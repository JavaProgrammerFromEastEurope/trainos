from ..message.message import Message


class CommunicationProtocol:

    def format(self, message: Message) -> str:
        return f"{message.sender}:{message.content}"
