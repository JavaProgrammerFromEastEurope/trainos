from dataclasses import dataclass

from .command_metadata import CommandMetadata
from .context_state import ContextState


@dataclass(frozen=True, slots=True)
class CommandContext:

    command_id: str
    metadata: CommandMetadata
    state: ContextState = ContextState.CREATED
