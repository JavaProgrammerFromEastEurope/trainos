from dataclasses import dataclass

from .account_owner import AccountOwner


@dataclass(frozen=True)
class Account:

    account_id: 	str
    owner_id: 		str
    owner_type: AccountOwner
    currency_id: 	str
