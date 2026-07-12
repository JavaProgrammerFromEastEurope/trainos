from kernel.persistence.transactions.transaction_engine import TransactionEngine
from kernel.persistence.transactions.transaction_status import TransactionStatus


def test_transaction():

    engine = TransactionEngine()
    transaction = engine.start("TX1")

    assert transaction.status == TransactionStatus.ACTIVE
    transaction = engine.commit(transaction)
    assert transaction.status == TransactionStatus.COMMITTED
    transaction = engine.start("TX2")
    transaction = engine.rollback(transaction)
    assert transaction.status == TransactionStatus.ROLLED_BACK
