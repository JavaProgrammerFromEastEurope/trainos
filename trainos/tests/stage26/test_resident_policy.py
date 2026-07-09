from kernel.population.residents.resident_policy import ResidentPolicy


def test_resident_policy():

    policy = ResidentPolicy(
        allow_employment	=	True,
        allow_consumption	=	True,
        allow_relocation	=	True,
    )

    assert policy.allow_employment 	is True
    assert policy.allow_consumption is True
    assert policy.allow_relocation 	is True