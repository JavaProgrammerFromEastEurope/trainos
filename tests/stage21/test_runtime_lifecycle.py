from kernel.core.runtime.base_runtime import BaseRuntime
from kernel.core.runtime.base_engine import BaseEngine
from kernel.core.runtime.base_context import BaseContext
from kernel.core.runtime.lifecycle_state import LifecycleState


class DummyEngine(BaseEngine):

    def initialize(self, context: BaseContext):
        pass

    def update(self, context: BaseContext, *args, **kwargs):
        pass

    def shutdown(self, context: BaseContext):
        pass


def test_runtime_lifecycle():

    runtime = BaseRuntime(DummyEngine())
    runtime.initialize()
    assert runtime.context.lifecycle.state == LifecycleState.INITIALIZED
    runtime.start()
    assert runtime.context.lifecycle.state == LifecycleState.RUNNING
    runtime.stop()
    assert runtime.context.lifecycle.state == LifecycleState.STOPPED
    runtime.shutdown()
    assert runtime.context.lifecycle.state == LifecycleState.SHUTDOWN

    first = BaseContext()
    second = BaseContext()
    first.lifecycle.transition(LifecycleState.RUNNING)
    assert first.lifecycle.state == LifecycleState.RUNNING
    assert second.lifecycle.state == LifecycleState.CREATED
    assert first.lifecycle is not second.lifecycle
