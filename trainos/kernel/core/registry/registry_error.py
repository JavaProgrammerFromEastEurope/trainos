class RegistryError(Exception):
    pass


class EntityNotFoundError(RegistryError):
    pass


class EntityAlreadyExistsError(RegistryError):
    pass
