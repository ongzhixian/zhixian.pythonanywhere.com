# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
from forum_app import app

from forum_app.features.dice import DiceFeature

@app.route('/api/dice/roll/<notation>', methods=['GET', 'POST'])
def api_dice_roll(notation):
    dice = DiceFeature()
    result = dice.roll(notation)

    if result is None:
        return "Bad request", 400
    else:
        return str(result)


@app.route('/api/dice/test/<notation>/<target>', methods=['GET', 'POST'])
def api_dice_test(notation, target):
    dice = DiceFeature()
    # logging.debug(f"api_dice_test {notation}, {target}")
    roll_count = dice.test_dice_rolls(notation, target)
    return str(roll_count), 200