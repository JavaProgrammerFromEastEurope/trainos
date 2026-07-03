from decimal import Decimal

from .ledger import Ledger


class BalanceCalculator:

    def balance(
        self,
        ledger: Ledger,
        account_id: str,
    ) -> Decimal:
        total = Decimal("0")
        for tx in ledger.entries():
            if tx.to_account == account_id:
                total += tx.amount
            if tx.from_account == account_id:
                total -= tx.amount
        return total
