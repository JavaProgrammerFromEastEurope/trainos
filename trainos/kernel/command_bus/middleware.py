from __future__ import annotations

from typing import Protocol

from .request 	import Request
from .response 	import Response


class Middleware(Protocol):

    def handle(
        self,
        request: Request,
        next_call,
    ) -> Response: ...
