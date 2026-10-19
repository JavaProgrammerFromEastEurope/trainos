from kernel.integration.adapters.adapter_engine import AdapterEngine


def test_adapter():

    payload = {"resident": "John"}
    result = AdapterEngine().adapt(payload)
    assert result.success is True
    assert result.payload == payload
