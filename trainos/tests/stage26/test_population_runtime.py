from kernel.population.runtime.population_runtime import PopulationRuntime


def test_population_runtime():

    runtime = PopulationRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None