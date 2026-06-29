from .reasoning_message import ReasoningMessage


class DistributedReasoningEngine:

    def exchange(self, message: ReasoningMessage) -> ReasoningMessage:
        return message
