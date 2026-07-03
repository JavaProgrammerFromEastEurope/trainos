from .tax_assessment import TaxAssessment


class TaxCollector:

    def collect(
        self,
        assessment: TaxAssessment,
    ) -> TaxAssessment:
        return assessment