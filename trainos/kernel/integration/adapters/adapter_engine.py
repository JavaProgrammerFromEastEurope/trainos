from .adapter_result import AdapterResult


class AdapterEngine:

    def adapt(
        self,
        payload: object,
    ) -> AdapterResult:
        return AdapterResult(
            success=True,
            payload=payload,
        )
