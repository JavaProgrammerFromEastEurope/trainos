from __future__ import annotations

from .meme import Meme


class MemeRegistry:

    def __init__(self) -> None:
        self._memes: list[Meme] = []

    def add(self, meme: Meme) -> None:
        self._memes.append(meme)

    def memes(self) -> tuple[Meme, ...]:
        return tuple(self._memes)
