from enum import Enum


class AuditStatus(Enum):

    PUBLISHED = "published"
    DELIVERED = "delivered"
    FAILED 		= "failed"