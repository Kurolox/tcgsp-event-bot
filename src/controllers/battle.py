
from discord import User

from schemas.battle import Battle
from controllers import tamer, transaction


def begin(attacker: User, defender: User, bet: int):
    attacker_tamer, defender_tamer = tamer.get(attacker), tamer.get(defender)

    for battling_tamer in [attacker_tamer, defender_tamer]:
        # Create the transaction for both players before starting the battle
        transaction.create(battling_tamer, - bet, "Challenge declaration")

        # Update the battle status of the tamers
        tamer.set_battle_status(battling_tamer, True)

    # Record the battle in the database
    Battle.create(
        attacker = attacker_tamer,
        defender = defender_tamer,
        wager = bet
    )
