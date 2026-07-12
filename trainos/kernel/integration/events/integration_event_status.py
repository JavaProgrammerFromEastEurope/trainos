from enum import Enum


class IntegrationEventStatus(Enum):

    CREATED 	= "created"
    PUBLISHED = "published"
    PROCESSED = "processed"