from dataclasses import dataclass
from decimal import Decimal

from .transfer_status import TransferStatus


@dataclass(frozen=True, slots=True)
class ResourceTransfer:

    transfer_id: 			str
    resource_id: 			str
    source_owner_id: 	str
    destination_owner_id: str
    quantity: Decimal
    status: TransferStatus