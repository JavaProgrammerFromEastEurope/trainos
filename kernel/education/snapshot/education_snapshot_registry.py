from kernel.core.registry.base_registry import BaseRegistry

from .education_snapshot import EducationSnapshot


class EducationSnapshotRegistry(
    BaseRegistry[EducationSnapshot],
):
    pass
