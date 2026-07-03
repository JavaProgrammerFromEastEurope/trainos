from dataclasses import dataclass


@dataclass(frozen=True)
class AccountView:

    account_id: 	str
    owner_id: 		str
    currency_id: 	str