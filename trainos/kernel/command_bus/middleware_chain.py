from __future__ import annotations

from typing import Callable, List

from .request 		import Request
from .response 		import Response
from .middleware 	import Middleware


class MiddlewareChain:

    def __init__(
        self,
        middlewares: List[Middleware],
        final_handler: Callable[[Request], Response],
    ) -> None:
        self._middlewares 	= middlewares
        self._final_handler = final_handler
    def execute(
        self,
        request: Request,
    ) -> Response:
        def build_chain(index: int):
            if index == len(self._middlewares):
                return lambda req: self._final_handler(req)
            current = self._middlewares[index]
            return lambda req: current.handle(
                req,
                build_chain(index + 1),
            )
        chain = build_chain(0)
        return chain(request)