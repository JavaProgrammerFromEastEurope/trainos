from .meme import Meme
from .meme_mutation import MemeMutation


class MemeticEngine:

    def mutate(self, meme: Meme) -> MemeMutation:
        return MemeMutation(
            original=meme.content,
            mutated=f"{meme.content}_v2",
        )
