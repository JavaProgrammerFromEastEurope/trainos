from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class TaxAssessment:

    assessment_id: 	str
    account_id: 		str
    tax_id: 				str
    taxable_amount: Decimal
    tax_amount: Decimal