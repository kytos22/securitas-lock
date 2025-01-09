from homeassistant import config_entries
from .const import DOMAIN, CONF_USERNAME, CONF_PASSWORD, CONF_NUMINST, CONF_PANEL

class SecuritasLockConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Securitas Lock."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            # Aquí puedes validar la entrada del usuario, como las credenciales
            return self.async_create_entry(title="Securitas Lock", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=self._get_schema(),
            errors=errors,
        )

    def _get_schema(self):
        from homeassistant.helpers.selector import TextSelector, TextSelectorConfig

        return {
            CONF_USERNAME: TextSelector(TextSelectorConfig(type="text")),
            CONF_PASSWORD: TextSelector(TextSelectorConfig(type="password")),
            CONF_NUMINST: TextSelector(TextSelectorConfig(type="text")),
            CONF_PANEL: TextSelector(TextSelectorConfig(type="text")),
        }
