class SecuritasAPI:
    def __init__(self, username, password, numinst, panel):
        self.username = username
        self.password = password
        self.numinst = numinst
        self.panel = panel

    async def lock(self):
        # Implementa la lógica para bloquear la cerradura
        pass

    async def unlock(self):
        # Implementa la lógica para desbloquear la cerradura
        pass

    async def get_lock_status(self):
        # Implementa la lógica para consultar el estado de la cerradura
        pass
