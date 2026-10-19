from dataclasses import dataclass


@dataclass(frozen=True)
class GuardianPolicy:

    may_block_execution: 	bool
    may_request_review: 	bool