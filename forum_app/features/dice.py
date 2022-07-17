import re
import secrets

import random
from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface

class DiceFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Dice"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable dice module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__)


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


    # Feature specific functions

    def parse_dice_notation(self, notation):
        notation_regex = r"(?P<num>\d+)?[d|D](?P<side>\d+)"
    
        m = re.match(notation_regex, notation)

        if m is None:
            return (1, 6)

        num_str = m.group('num')
        side_str = m.group('side')
        num = int(num_str) if num_str is not None and num_str.isdigit() else 1
        side = int(side_str) if side_str is not None and side_str.isdigit() else 6

        log.debug(f"{num}D{side}")
        return (num, side)

    def roll_secret_dice(number_of_dice, dice_side):
        """Randomness based on 'secrets' modules"""
        total = 0
        for _ in range(number_of_dice):
            out_come = secrets.choice(range(1, dice_side + 1))
            total = total + out_come
            # log.debug(f"outcome: {out_come}, total: {total}")
        return total

    def roll_random_choice_dice(number_of_dice, dice_side):
        """Randomness based on 'random.choice'"""
        total = 0
        for _ in range(number_of_dice):
            out_come = random.choice(range(1, dice_side + 1))
            total = total + out_come
            # log.debug(f"outcome: {out_come}, total: {total}")
        return total

    def roll_random_dice(number_of_dice, dice_side):
        """Randomness based on 'random.choice'"""
        total = 0
        for _ in range(number_of_dice):
            out_come = random.randrange(1, dice_side + 1)
            total = total + out_come
            # log.debug(f"outcome: {out_come}, total: {total}")
        return total

    # def roll_random_dice(number_of_dice, dice_side):
    #     """Randomness based on 'randint'"""
    #     total = 0
    #     for _ in range(number_of_dice):
    #         out_come = random.choice(range(1, dice_side + 1))
    #         total = total + out_come
    #         # log.debug(f"outcome: {out_come}, total: {total}")
    #     return total

    def roll(self, notation):
        (num, side) = self.parse_dice_notation(notation)

        if num is None:
            return 0

        total = DiceFeature.roll_secret_dice(num, side)

        log.debug(f"{num}D{side},  {total}")
        return total
        
    def test_dice_rolls(self, notation, target_number):
        target = int(target_number)

        (num, side) = self.parse_dice_notation(notation)
        
        if num is None:
            return -1

        if (target > (num * side)) or (target < (num * side)):
            return -1
        
        roll_count = 0
        current_roll = 0
        while current_roll != target:
            current_roll = DiceFeature.roll_random_dice(num, side)
            roll_count = roll_count + 1
        log.debug(f"{roll_count} rolls to get a {target_number} on {notation}")
        return roll_count