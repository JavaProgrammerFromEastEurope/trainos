from trainos.kernel.evolution.memetics.ideology.ideology_engine import IdeologyEngine


def test_ideology_engine_form_cluster():

    engine = IdeologyEngine()

    cluster = engine.form_cluster(
        "sustainability",
    )

    assert cluster.name == "sustainability"