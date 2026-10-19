from kernel.configuration.providers.default_provider import DefaultProvider


def test_default_provider():

    provider 	= DefaultProvider()
    result 		= provider.load(123)
    assert result == 123
