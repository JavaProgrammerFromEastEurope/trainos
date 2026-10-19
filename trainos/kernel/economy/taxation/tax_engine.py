from decimal import Decimal

from .tax_assessment import TaxAssessment
from .tax_definition import TaxDefinition


class TaxEngine:

    def calculate(
        self,
        account_id: str,
        taxable_amount: Decimal,
        definition: TaxDefinition,
    ) -> TaxAssessment:
        tax = taxable_amount * definition.rate

        return TaxAssessment(
            assessment_id="AUTO",
            account_id=account_id,
            tax_id=definition.tax_id,
            taxable_amount=taxable_amount,
            tax_amount=tax,
        )
