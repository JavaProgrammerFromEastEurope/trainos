from dataclasses import dataclass

from .resources_configuration import ResourcesConfiguration


@dataclass(slots=True)
class ResourcesContext:

    configuration: ResourcesConfiguration