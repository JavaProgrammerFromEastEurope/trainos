from trainos.kernel.civilization.civilization.civilization_engine import CivilizationEngine
from trainos.kernel.civilization.culture.cultural_memory import CulturalMemory
from trainos.kernel.civilization.culture.cultural_record import CulturalRecord
from trainos.kernel.civilization.ethics.ethics_engine import EthicsEngine
from trainos.kernel.civilization.history.historical_record import HistoricalRecord
from trainos.kernel.civilization.history.history_registry import HistoryRegistry
from trainos.kernel.civilization.identity.identity import Identity
from trainos.kernel.civilization.identity.identity_registry import IdentityRegistry
from trainos.kernel.civilization.identity.identity_type import IdentityType
from trainos.kernel.civilization.myth.myth import Myth
from trainos.kernel.civilization.myth.myth_registry import MythRegistry
from trainos.kernel.civilization.myth.myth_type import MythType
from trainos.kernel.civilization.reputation.reputation_engine import ReputationEngine
from trainos.kernel.civilization.tradition.tradition import Tradition
from trainos.kernel.civilization.tradition.tradition_registry import TraditionRegistry
from trainos.kernel.civilization.tradition.tradition_type import TraditionType
from trainos.kernel.civilization.value.value_engine import ValueEngine


def test_stage10_full_pipeline():

    # Cultural memory
    memory = CulturalMemory()
    memory.add(CulturalRecord(description="event"))

    # Tradition
    tradition_registry = TraditionRegistry()
    tradition_registry.add(
        Tradition(type=TraditionType.FOOD_RESERVE)
    )

    # History
    history = HistoryRegistry()
    history.add(HistoricalRecord(description="survival"))

    # Identity
    identity_registry = IdentityRegistry()
    identity_registry.add(
        Identity(type=IdentityType.BUILDER)
    )

    # Myth
    myth_registry = MythRegistry()
    myth_registry.add(
        Myth(type=MythType.FOUNDING)
    )

    # Reputation
    reputation = ReputationEngine().evaluate()

    # Values
    value = ValueEngine().determine()

    # Ethics
    ethics = EthicsEngine().evaluate()

    # Civilization
    civilization = CivilizationEngine().run()

    assert len(memory.records()) == 1
    assert len(tradition_registry.traditions()) == 1
    assert len(history.records()) == 1
    assert len(identity_registry.identities()) == 1
    assert len(myth_registry.myths()) == 1
    assert reputation.score is not None
    assert value.type is not None
    assert ethics.type is not None
    assert civilization.state is not None