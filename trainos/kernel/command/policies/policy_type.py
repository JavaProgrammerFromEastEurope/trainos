from enum import Enum


class PolicyType(Enum):

    FAIL_FAST = "fail_fast"
    RETRY = "retry"
    NO_RETRY = "no_retry"
    REQUIRE_CONFIRMATION = "require_confirmation"
