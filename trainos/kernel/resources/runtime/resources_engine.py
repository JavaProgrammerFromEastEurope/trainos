from .resources_context import ResourcesContext


class ResourcesEngine:

    def initialize(
        self,
        context: ResourcesContext,
    ) -> None:
        pass

    def update(
        self,
        context: ResourcesContext,
    ) -> None:
        pass

    def shutdown(
        self,
        context: ResourcesContext,
    ) -> None:
        pass
