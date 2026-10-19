from dataclasses import FrozenInstanceError

import pytest

from kernel.economy.treasury.treasury import Treasury
from kernel.economy.treasury.treasury_engine import TreasuryEngine


def test_treasury():

    treasury = Treasury(
        treasury_id="TREASURY-001",
        government_id="GOV-001",
        primary_account_id="ACC-TREASURY-001",
    )

    engine = TreasuryEngine()

    result = engine.validate(treasury)

    assert result is treasury

    assert result.treasury_id == "TREASURY-001"
    assert result.government_id == "GOV-001"
    assert result.primary_account_id == "ACC-TREASURY-001"

    with pytest.raises(FrozenInstanceError):
        result.primary_account_id = "ACC-TREASURY-002"