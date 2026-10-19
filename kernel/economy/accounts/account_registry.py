from __future__ import annotations

from .account import Account


class AccountRegistry:

    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def register(self, account: Account) -> None:
        self._accounts[account.account_id] = account

    def get(self, account_id: str) -> Account | None:
        return self._accounts.get(account_id)

    def all(self) -> tuple[Account, ...]:
        return tuple(self._accounts.values())
