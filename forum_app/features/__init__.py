################################################################################
# Define package composition
################################################################################

# Note: The sequence is important. Dependents should be loaded after the parent feature
__all__ = [
    "authentication", "login", "user_profile",
    "role_based_access_control", "role", "permission",
    "development", "development_note",
    "trade"

    # "investment_client", "investment_portfolio", 
    # Not ready yet
    # "inventory",
    # "human_resource"
    # "education"
    # "shared_data","iso_data", "financial_instrument_data",
    # "note", "tag",
    # "game", "dice", "card"
    ]

import logging
from forum_app.modules import app_state
from forum_app.databases.mysql_data_provider import MySqlDataProvider

def is_feature_enable(feature_name):
    """Check if feature is enable"""
    if feature_name not in app_state.feature:
        return False
    return app_state.feature[feature_name]['is_enable']

class BaseFeatureInterface:
    """Defines interface for feature"""

    def __init__(self):
        self.db = MySqlDataProvider('forum')
    
    def is_registered(self, feature_name) -> bool:
        """Check if feature is registered in system (inherited; use by all features)"""
        record = self.db.fetch_record(
            "SELECT 1 FROM _feature WHERE display_name = %s;", 
            (feature_name,))
        if record is None:
            return False
        return True

    def register_feature(self, feature_name, feature_description, module_name, parent_name=None) -> bool:
        """Register feature into system (inherited; use by all features)"""
        normalized_name = feature_name.replace(' ', '-').lower()
        # normalized_parent_name = parent_name.replace(' ', '-').lower()

        if parent_name is None:
            (rows_affected, _) = self.db.execute(
                "INSERT INTO _feature (name, display_name, description, module_name, level) VALUES (%s, %s, %s, %s, 0);", 
                (feature_name.replace(' ', '-').lower(), feature_name, feature_description, module_name))
        else:
            sql = """
INSERT INTO _feature (name, display_name, description, module_name, level, parent_id, root_parent_id)
SELECT  %s          AS `name`
        , %s        AS `display_name`
        , %s        AS `description`
        , %s        AS 'module_name'
        , level + 1 AS 'level'
        , id        AS 'parent_id'
        , COALESCE(root_parent_id, id)  AS 'root_parent_id'
FROM    _feature c
WHERE   display_name = %s

        """
            (rows_affected, _) = self.db.execute(
                sql, 
                (normalized_name, feature_name, feature_description, module_name, parent_name))
        logging.debug(f"register_feature ({feature_name}): {rows_affected}")
        return rows_affected > 0

    def update_is_enable(self, feature_name, enable):
        """Called by toggle_enable (general-usage)"""
        (rows_affected, _) = self.db.execute("""
UPDATE  _feature 
SET		is_enable = %s
WHERE	name = %s;
""", (enable, feature_name))
        return rows_affected

    def toggle_enable(self, feature_name, enable):
        """Update is_enable flag for feature API (use by feature dashboard) (general-usage)"""
        rows_affected = self.update_is_enable(feature_name, enable)
        changes_saved = rows_affected > 0
        if changes_saved:
            app_state.enable_feature(feature_name, enable)
            # app_state.feature[feature_name]['is_enable'] = enable
            # app_events['app_state_changed']('toggle_enable')
            logging.debug(f"{feature_name} is_enable set to {enable}, changes_saved={changes_saved} ")
        return changes_saved


    def register(self):
        """Register feature into system (required)"""
        pass

    def get_enable_setting_by_name(self, name):
        """Called by initialize (on initialize_features)"""
        record = self.db.fetch_record(
            "SELECT is_enable, module_name FROM _feature WHERE name = %s;", 
            (name,))
        if record is None:
            return (None, None)
        return (record[0], record[1])

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        # TODO: restore state from persistence storage
        (is_enable, _) = self.get_enable_setting_by_name(self.feature_name)
        if is_enable is None:
            is_enable = False
        app_state.feature[self.feature_name] = {
            "is_enable" : is_enable
        }

    def app_state_changed(self, event_data=None):
        """Things to do whenever app_state changed"""
        pass

    def is_my_event(self, event_data=None):
        if event_data is None:
            return False # Only handle when there's event_data
        if 'feature_name' not in event_data:
            return False # Only handle when we identify source
        if event_data['feature_name'] == '__ALL_FEATURES__':
            return True  # Only handle events when it concerns ALL
        if event_data['feature_name'] != self.feature_name:
            return False # Only handle events when it concerns us
        return True

    # def get_enable_setting(self, module_name):
    #     record = self.db.fetch_record(
    #         "SELECT is_enable FROM _feature WHERE module_name = %s;", 
    #         (module_name,))
    #     if record is None:
    #         return False
    #     return record[0] == 1

    # def load(self):
    #     """Things to do whenever feature is loaded"""
    #     pass

    # def load_app_settings(self, app_settings):
    #     """Load app_settings (from storage) """
    #     pass

    # def update_app_settings(self, app_settings):
    #     """Define/Set app_settings """
    #     pass
    
    # Properties

    # @property
    # def is_valid_feature(self):
    #     """is_valid_feature getter property. (required)
    #     Ensures that required properties are not None: feature_name, feature_description
    #     """
    #     return self.feature_name is not None and self.feature_description is not None

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return None

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return None

    @property
    def is_enable(self):
        """is_enable getter property. (inherited)"""
        return app_state.feature[self.feature_name]['is_enable']

    @is_enable.setter
    def is_enable(self, value):
        """is_enable setter property. (inherited)"""
        app_state.feature[self.feature_name]['is_enable'] = value

    # @is_enable.deleter
    # def is_enable(self):
    #     """is_enable deleter property."""
    #     del self._is_enable

class BaseMenuInterface:
    """Defines interface for menu"""

    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def add_menu_item(self, display_name, description, href=None, parent_name=None):
        sql = """
INSERT INTO _menu (display_name, href, description, level, parent_id, ancestor_id, display_order)
SELECT  DISTINCT
        %s AS 'display_name'
        , %s AS 'href'
        , %s AS 'description'
        , level + 1 AS 'level'
        , id AS 'parent_id'
        , COALESCE(ancestor_id, id) AS 'ancestor_id'
        , (
            SELECT  COALESCE(MAX(display_order) + 1, 1) AS 'display_order'
            FROM    _menu 
            WHERE   parent_id = (SELECT id FROM _menu WHERE display_name = %s)
        ) AS 'display_order'
FROM    _menu
WHERE   _menu.display_name = %s;
"""
        self.db.execute(sql, (display_name, href, description, parent_name, parent_name))

        # href, level, display_order,
#         if parent_name is None:
#             sql = """
# INSERT INTO _menu (display_name, href, description, level, parent_id, ancestor_id, display_order)
# SELECT  DISTINCT
#         %s AS 'display_name'
#         , NULL AS 'href'
#         , s AS 'description'
#         , 0 AS 'level'
#         , NULL AS 'parent_id'
#         , NULL AS 'ancestor_id'
#         , MAX(display_order) + 1 AS 'display_order'
# FROM    _menu
# GROUP BY _menu.level
#             """
#             self.db.execute(sql, (display_name, description))
#         else:


    
    def get_menu_items(self) -> bool:
        """Get menu items"""
        sql = """
SELECT  c.id
        , c.display_name
        , c.href, c.description
        , COALESCE(p.display_name, c.display_name) as 'parent_name'
        , COALESCE(p.display_order, c.display_order) AS 'parent_display_order'
        , c.display_order
FROM    _menu c
LEFT OUTER JOIN
        _menu p
        ON c.parent_id = p.id
ORDER BY COALESCE(p.display_order, c.display_order) 
        """
        records = self.db.fetch_list(sql, None)
        return [] if records is None else records