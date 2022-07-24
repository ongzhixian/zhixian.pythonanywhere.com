################################################################################
# Define package composition
################################################################################

__all__ = ["barcode", "feature"
    # , "user", "login", "role"
]

import json
import logging

class app_state(object):
    
    feature = {}
    menu = {}
    value = {}
    event = {}
    is_development = False
    
    def add_menu_callback(menu_name, callback):
        """Used only app initialization; no logging needed"""
        app_state.menu[menu_name] = callback()

    def add_to_menu(menu_name, menu_item_id, display_text, href=None, is_disabled=False, icon_name=None):
        if menu_name not in app_state.menu:
            return
        
        menu = app_state.menu[menu_name]
        
        logging.info(f"Add to menu {menu_name} menu item {menu_item_id}")
        menu.add_menu_item(menu_item_id, display_text, href, is_disabled, icon_name)

    def remove_from_menu(menu_name, menu_item_id):
        if menu_name not in app_state.menu:
            return
        
        menu = app_state.menu[menu_name]
        
        logging.info(f"Remove from menu {menu_name} menu item {menu_item_id}")
        menu.remove_menu_item(menu_item_id)

    def add_value(key, value):
        """Used only app initialization; no logging needed"""
        app_state.value[key] = value

    def add_event_callback(event_name, callback):
        """Used only app initialization; no logging needed"""
        app_state.event[event_name] = callback

    def enable_feature(feature_name, enable):
        logging.info(f"{feature_name} is_enable set to {enable}")
        app_state.feature[feature_name]['is_enable'] = enable
        app_state.event['app_state_changed'](
            {
                "feature_name": feature_name,
                "is_enable": enable
            })
        # app_events['app_state_changed']('toggle_enable')

    # def __init__(self):
    #     pass

    # @property
    # def feature(self):
    #     """feature getter property. (inherited)"""
    #     return app_state._feature


    # @property
    # def menu(self):
    #     """menu getter property. (inherited)"""
    #     return app_state._menu
    #     # return app_state['feature'][self.feature_name]['is_enable']


    # @menu.setter
    # def menu(self, value):
    #     """menu setter property. (inherited)"""
    #     app_state._menu = value
    #     # app_state['feature'][self.feature_name]['is_enable'] = value



# def initialize_app_state():
#     from forum_app.modules import app_state
#     app_statex = app_state()
#     app_state = {}
#     app_state['feature'] = {}
#     app_state['menu'] = {
#         'drawer_sitemap_menu' : setup_drawer_sitemap_menu(),
#         'drawer_admin_menu' : setup_drawer_admin_menu(),
#         'header_menu' : setup_header_menu(),
#     }
#     # app_state['drawer_sitemap_menu'] = setup_drawer_sitemap_menu()
#     # app_state['drawer_admin_menu'] = setup_drawer_admin_menu()
#     # app_state['header_menu'] = setup_header_menu()
#     app_state['selected_application'] = None
#     app_state['menu']['application_menu'] = setup_application_menu()
#     app_state['menu']['login_menu'] = setup_login_menu()
#     # app_state['application_menu'] = setup_application_menu()
#     return app_state


# Logging

class structured_log_message(object):
    """Structured logging message

    **Usage**

    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logging.info(_('message 1', foo='bar', bar='baz', num=123, fnum=123.456))

    **Reference**
    
    https://docs.python.org/3/howto/logging-cookbook.html#implementing-structured-logging
    """
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return '%s | %s' % (self.message, json.dumps(self.kwargs))

class log(object):
    def critical(message, **kwargs):
        logging.critical(structured_log_message(message, **kwargs))

    def error(message, **kwargs):
        logging.error(structured_log_message(message, **kwargs))

    def exception(message, **kwargs):
        logging.exception(structured_log_message(message, **kwargs))

    def warning(message, **kwargs):
        logging.warning(structured_log_message(message, **kwargs))

    def info(message, **kwargs):
        logging.info(structured_log_message(message, **kwargs))

    def debug(message, **kwargs):
        logging.debug(structured_log_message(message, **kwargs))

    