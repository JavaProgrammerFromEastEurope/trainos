from dataclasses import dataclass

from kernel.resources.definitions.resource_definition import ResourceDefinition


@dataclass(frozen=True)
class ResourceRecord:

    resource_id: str
    definition: ResourceDefinition