from dataclasses import dataclass


@dataclass(frozen=True)
class Treasury:

    treasury_id: 				str
    government_id: 			str
    primary_account_id: str