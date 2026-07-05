from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from kernel.economy.transactions.transaction import Transaction
from kernel.economy.transactions.transaction_engine import TransactionEngine
from kernel.economy.transactions.transaction_type import TransactionType


def test_transaction_engine_validate():

    engine = TransactionEngine()

    transaction = Transaction(
        transaction_id="TX-0001",
        from_account="ACC-0001",
        to_account="ACC-0002",
        amount=Decimal("25.00"),
        currency_id="currency-trc",
        transaction_type=TransactionType.TRANSFER,
    )

    result = engine.validate(transaction)

    assert result is transaction

    assert result.transaction_id == "TX-0001"
    assert result.from_account == "ACC-0001"
    assert result.to_account == "ACC-0002"
    assert result.amount == Decimal("25.00")
    assert result.currency_id == "currency-trc"
    assert result.transaction_type == TransactionType.TRANSFER

    with pytest.raises(FrozenInstanceError):
        result.amount = Decimal("100.00")