# kernel/kernel.py

from __future__ import annotations

from typing import Dict, Optional, List
from trainos.kernel.lifecycle.kernel_service import KernelService, ServiceState
from trainos.kernel.events.event_bus import EventBus
from trainos.kernel.logging.logger import Logger
from trainos.kernel.clock.clock_service import ClockService
from trainos.kernel.time.time_service import TimeService


class Kernel:

	def __init__(
			self,
			logger: Optional[Logger] = None,
	) -> None:

			self._services: Dict[str, KernelService] = {}
			self._event_bus = EventBus()
			self._logger = logger
			self._running = False

	@property
	def event_bus(self) -> EventBus:
			return self._event_bus

	@property
	def logger(self) -> Optional[Logger]:
			return self._logger

	def register_service(self, service: KernelService) -> None:

			if service.name in self._services:
					raise ValueError(f"Service already registered: {service.name}")
			self._services[service.name] = service

	def get_service(self, name: str) -> KernelService:

			if name not in self._services:
					raise KeyError(f"Service not found: {name}")
			return self._services[name]

	def initialize(self) -> None:

			ordered = self._resolve_startup_order()
			for service in ordered:
					service.initialize()
					if self._logger:
							self._logger.info(
									source="Kernel",
									message=f"Initialized service {service.name}",
									timestamp=0.0,
							)

	def start(self) -> None:
			ordered = self._resolve_startup_order()
			for service in ordered:
					service.start()

			self._running = True

	def stop(self) -> None:
			ordered = reversed(self._resolve_startup_order())
			for service in ordered:
					service.stop()

			self._running = False

	def update(self, dt: float) -> None:
			if not self._running:
					return
			for service in self._services.values():
					if service.state == ServiceState.RUNNING:
							service.update(dt)
			self._event_bus.update()

	def dispose(self) -> None:
			for service in self._services.values():
					service.dispose()
			self._services.clear()

	def bootstrap(self) -> "Kernel":
			"""
			Stage 1 compatibility entry point.

			Wraps full initialization lifecycle:
			register -> initialize -> start
			"""

			if self._running:
					return self

			self.initialize()
			self.start()

			return self
	def is_booted(self) -> bool:
			return self._running

	def _resolve_startup_order(self) -> List[KernelService]:
			resolved: List[KernelService] = []
			unresolved: set[str] = set()

			def resolve(service: KernelService) -> None:
					if service.name in unresolved:
							raise RuntimeError("Circular dependency detected")
					if service in resolved:
							return
					unresolved.add(service.name)
					for dep_name in service.dependencies:
							dep = self._services.get(dep_name)
							if not dep:
									raise KeyError(f"Missing dependency: {dep_name}")
							resolve(dep)
					unresolved.remove(service.name)
					resolved.append(service)

			for service in self._services.values():
					resolve(service)
			return resolved
