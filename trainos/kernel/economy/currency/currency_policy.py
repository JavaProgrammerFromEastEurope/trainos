from dataclasses import dataclass


@dataclass(frozen=True)
class CurrencyPolicy:

    allow_duplicate_codes: 	bool
    immutable_currency: 		bool