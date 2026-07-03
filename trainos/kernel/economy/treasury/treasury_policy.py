from dataclasses import dataclass


@dataclass(frozen=True)
class TreasuryPolicy:

    allow_multiple_treasuries: bool
    immutable_primary_account: bool