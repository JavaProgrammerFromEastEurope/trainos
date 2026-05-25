from trainos.core.module import BaseModule


class ModuleManager:

    def __init__(self):
        self.modules: dict[str, BaseModule] = {}

    def register(self, module: BaseModule):
        self.modules[module.name] = module

    def start_all(self):

        for module in self.modules.values():
            module.start()

    def update_all(self):

        for module in self.modules.values():
            module.update()

    def shutdown_all(self):

        for module in self.modules.values():
            module.shutdown()
