from kernel.persistence.contracts.persistence_contract 	import PersistenceContract
from kernel.persistence.contracts.persistence_type 			import PersistenceType


def test_persistence_contract():

    contract = PersistenceContract(
        object_id="OBJ-001",
        persistence_type=PersistenceType.ENTITY,
        version=1,
    )
    assert contract.object_id == "OBJ-001"
    assert contract.persistence_type == PersistenceType.ENTITY
    assert contract.version == 1
