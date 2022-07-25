from os import path
from forum_app import app_path
from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface, BaseMenuInterface

class TradeInstrumentFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Trade Instrument"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable trade instrument module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()
        self.add_oda_instruments()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'trade_instrument', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        # No UI access point
        # BaseMenuInterface().add_menu_item('Trade', 'Trade module', '/trade/dashboard', 'Applications')
        # self.register_feature(self.feature_name, self.feature_description, __name__)

    def update_ui(self):
        # We want to selective add/remove logins menu item to admin menu in drawer
        # menu_item_id = "shared-data-dashboard"
        #
        # if self.is_enable:
        #     logging.debug("Add to drawer_admin_menu")
        #     app_state.add_to_menu('drawer_admin_menu', menu_item_id, "Shared data", "/shared-data/dashboard", False, "table_rows",)
        # else:
        #     # Remove login menu item to admin menu in drawer
        #     logging.debug("Remove drawer_admin_menu")
        #     app_state.remove_from_menu('drawer_admin_menu', menu_item_id)
        pass

    def app_state_changed(self, event_data=None):
        """Things to do whenever app_state changed"""
        if not self.is_my_event(event_data):
            return
        log.debug(f"{self.feature_name} is_enable: {self.is_enable} event_data {event_data}")
        self.update_ui()

    def get_records_from_csv_file(self, file_name):
        import csv
        csv_data_file_path = path.join(app_path, 'data', 'comma_separated_values', file_name)
        instrument_data = []
        with open(csv_data_file_path, "r", encoding="utf8") as in_file:
            csv_reader = csv.reader(in_file)
            # row 0 -- ticker
            # row 1 -- name
            # row 2 -- type
            # row 3 -- asset class
            # row 4 -- kid asset class
            for row in csv_reader:
                instrument_data.append((row[0], row[1], row[2], row[3], row[0]))
        return instrument_data

    # Feature specific methods
    def add_oda_instruments(self):
        # Read from CSV file and insert into database
        print('add_oda_instruments')
        instrument_data = self.get_records_from_csv_file('oda-simplified-instruments.csv')
        sql = """
INSERT INTO trade_instrument (ticker, name, type_id, asset_class, execution_venue)
SELECT 	DISTINCT 
        %s AS ticker
		, %s AS name
        , %s AS type_id
        , %s AS asset_class
        , 'ODA' AS execution_venue 
FROM    (SELECT 1) a
WHERE	NOT EXISTS (SELECT 1 FROM trade_instrument WHERE execution_venue = 'ODA' AND ticker = %s);
"""
        self.db.execute_many(sql, instrument_data)
        # for instrument in instrument_data:
        #     print(instrument)

    def get_instrument_count_by_asset_class(self):
        sql = """
SELECT	asset_class, COUNT(id) AS 'count'
FROM	trade_instrument 
GROUP BY asset_class
ORDER BY asset_class;
"""
        return self.db.fetch_list(sql)