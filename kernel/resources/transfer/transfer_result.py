from dataclasses import dataclass
from decimal import Decimal

from .transfer_status import TransferStatus


@dataclass(frozen=True, slots=True)
class TransferResult:

    transfer_id: 					str
    transferred_quantity: Decimal
    status: TransferStatus