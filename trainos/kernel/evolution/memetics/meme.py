from dataclasses import dataclass

from .meme_type import MemeType


@dataclass
class Meme:

    type: MemeType
    content: str