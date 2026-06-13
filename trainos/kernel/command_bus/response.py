from __future__ import annotations


class Response:

    def __init__(
        self,
        success: bool,
        data: object = None,
        error: str | None = None,
    ) -> None:
        self.success 	= success
        self.data 		= data
        self.error 		= error
