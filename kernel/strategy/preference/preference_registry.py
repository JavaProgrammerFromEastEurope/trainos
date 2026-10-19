from __future__ import annotations

from .preference_profile import PreferenceProfile


class PreferenceRegistry:

    def __init__(self) -> None:
        self._profiles: list[PreferenceProfile] = []

    def register(self, profile: PreferenceProfile) -> None:
        self._profiles.append(profile)

    def profiles(self) -> tuple[PreferenceProfile, ...]:
        return tuple(self._profiles)
