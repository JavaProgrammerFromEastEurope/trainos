from trainos.kernel.evolution.memetics.meme import Meme
from trainos.kernel.evolution.memetics.meme_type import MemeType
from trainos.kernel.evolution.memetics.memetic_engine import MemeticEngine


def test_memetic_engine_mutate():

    engine = MemeticEngine()

    meme = Meme(
        type=MemeType.BELIEF,
        content="cooperation",
    )

    mutation = engine.mutate(meme)

    assert mutation.original == "cooperation"
    assert mutation.mutated == "cooperation_v2"