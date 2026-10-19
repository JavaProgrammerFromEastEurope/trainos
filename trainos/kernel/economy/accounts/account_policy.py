from dataclasses import dataclass


@dataclass(frozen=True)
class AccountPolicy:

    allow_multiple_accounts: 	bool
    immutable_currency: 			bool