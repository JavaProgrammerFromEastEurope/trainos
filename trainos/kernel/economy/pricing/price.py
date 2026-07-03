from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Price:

    price_id: 		str
    subject_id: 	str
    currency_id: 	str
    amount: Decimal