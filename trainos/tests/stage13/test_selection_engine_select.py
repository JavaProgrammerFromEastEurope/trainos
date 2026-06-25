from trainos.kernel.evolution.memetics.selection.meme_fitness import MemeFitness
from trainos.kernel.evolution.memetics.selection.selection_engine import SelectionEngine


def test_selection_engine_select():

    engine = SelectionEngine()

    first = MemeFitness(
        meme="cooperation",
        score=0.9,
    )

    second = MemeFitness(
        meme="competition",
        score=0.3,
    )

    result = engine.select(
        first,
        second,
    )

    assert result.winner == "cooperation"
    assert result.loser == "competition"