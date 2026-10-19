from .authority_engine import AuthorityEngine


class AuthorityRuntime:

    def __init__(self) -> None:
        self._engine = AuthorityEngine()

    def initialize(self) -> None:
        pass

    def update(self, authority):
        return self._engine.assign(authority)

    def shutdown(self) -> None:
        pass
