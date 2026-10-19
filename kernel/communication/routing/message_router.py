from __future__ import annotations

from ..message.message import Message


class MessageRouter:

    def route(self, message: Message) -> str:
        return message.receiver
