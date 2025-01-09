from homeassistant.components.lock import LockEntity
from .const import DOMAIN

class SecuritasLock(LockEntity):
    """Representation of a Securitas Lock."""

    def __init__(self, name, api):
        self._name = name
        self._api = api
        self._is_locked = None

    @property
    def name(self):
        return self._name

    @property
    def is_locked(self):
        return self._is_locked

    async def async_lock(self, **kwargs):
        await self._api.lock()
        self._is_locked = True
        self.async_write_ha_state()

    async def async_unlock(self, **kwargs):
        await self._api.unlock()
        self._is_locked = False
        self.async_write_ha_state()

    async def async_update(self):
        self._is_locked = await self._api.get_lock_status()
