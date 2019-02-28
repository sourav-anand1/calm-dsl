from .entity import EntityType, Entity
from .validator import PropertyValidator


# Substrate

class SubstrateType(EntityType):
    __schema_name__ = "Substrate"


class SubstrateValidator(PropertyValidator, openapi_type="substrate"):
    __default__ = None
    __kind__ = SubstrateType


def substrate(**kwargs):
    name = getattr(SubstrateType, "__schema_name__")
    bases = (Entity, )
    return SubstrateType(name, bases, kwargs)


Substrate = substrate()
