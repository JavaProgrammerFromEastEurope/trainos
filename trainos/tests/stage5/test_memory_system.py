from trainos.kernel.ai.memory.memory_manager import MemoryManager


def test_memory_system():
    memory = MemoryManager()
    memory.working.set("hp", 100)
    assert memory.working.get("hp") == 100
