from .meme_fitness import MemeFitness
from .selection_event import SelectionEvent


class SelectionEngine:

    def select(
        self,
        first: MemeFitness,
        second: MemeFitness,
    ) -> SelectionEvent:

        if first.score >= second.score:
            return SelectionEvent(
                winner=first.meme,
                loser=second.meme,
            )
        return SelectionEvent(
            winner=second.meme,
            loser=first.meme,
        )
