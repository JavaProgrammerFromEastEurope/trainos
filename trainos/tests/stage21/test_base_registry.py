from kernel.core.registry.base_registry import BaseRegistry


def test_base_registry():

    registry = BaseRegistry[str]()
    registry.register("ID-1", "Hello")

    assert registry.exists("ID-1")
    assert registry.get("ID-1") == "Hello"

    registry.delete("ID-1")
    assert registry.exists("ID-1") is False
