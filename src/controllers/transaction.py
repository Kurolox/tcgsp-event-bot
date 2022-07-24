from controllers import tamer
from schemas.tamer import Tamer
from schemas.transaction import Transaction
from controllers import tamer as tamer_controller

def create(tamer: Tamer, movement: int, reason: str):

    # Update the tamers currency before creating the transaction
    tamer_controller.alter_currency(tamer, movement)

    # Write the transaction into the database for scorekeeping purposes
    Transaction.create(
        tamer = tamer.id,
        movement = movement,
        balance = tamer.currency,
        reason = reason
    )