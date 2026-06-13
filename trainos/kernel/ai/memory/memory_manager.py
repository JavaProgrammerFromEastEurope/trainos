from __future__ import annotations

from .working_memory import WorkingMemory
from .short_term_memory import ShortTermMemory
from .long_term_memory import LongTermMemory
from .episodic_memory import EpisodicMemory


class MemoryManager:

    def __init__(self) -> None:
        self.working 		= WorkingMemory()
        self.short_term = ShortTermMemory()
        self.long_term 	= LongTermMemory()
        self.episodic 	= EpisodicMemory()