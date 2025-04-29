
from universal_mcp.servers.server import SingleMCPServer
from universal_mcp.integrations.integration import ApiKeyIntegration
from universal_mcp.stores.store import EnvironmentStore

from universal_mcp_shortcut.app import ShortcutApp

env_store = EnvironmentStore()
integration_instance = ApiKeyIntegration(name="SHORTCUT_API_KEY", store=env_store)
app_instance = ShortcutApp(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()


