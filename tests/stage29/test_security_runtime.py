from kernel.security.runtime.security_runtime import SecurityRuntime


def test_security_runtime():

    runtime = SecurityRuntime()
    runtime.initialize()
    runtime.update()
    runtime.shutdown()

    assert runtime.context is not None