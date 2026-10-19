from .factory import Factory
from .factory_status import FactoryStatus


class FactoryEngine:

    def start(self, factory: Factory) -> Factory:
        return Factory(
            factory_id=factory.factory_id,
            name=factory.name,
            factory_type=factory.factory_type,
            status=FactoryStatus.ACTIVE,
        )

    def stop(self, factory: Factory) -> Factory:
        return Factory(
            factory_id=factory.factory_id,
            name=factory.name,
            factory_type=factory.factory_type,
            status=FactoryStatus.OFFLINE,
        )
