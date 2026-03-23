from mcp.servers.utilities.mcp.mcp_discovery import MCPDiscovery # type: ignore
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset # type: ignore
from google.adk.tools.mcp_tool import StdioConnectionParams # type: ignore
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams # type: ignore
from mcp import StdioServerParameters

class MCPConnector:
    """
    Discovers the MCP servers from the config.
    config will be loaded by the MCP's discovery class.
    Then it lists each server's tools and then caches them as MCPToolsets 
    that are compatible Google's Agent Development Kit (ADK).  
    """ 

    def __init__(self, config_file: str = None):
        self.discovery = MCPDiscovery(config_file = config_file)
        self.tools: list[MCPToolset] = []
        self.load_all_tools()

    async def load_all_tools(self):
        """
        Loads all tools from the discovered MCP servers and caches them as MCPToolsets.
        """

        tools = []

        for name, server in self.discovery.list_servers():
            try:
                if server.get("comand") == "streamable_http":
                    conn =  StreamableHTTPConnectionParams(url=server.get("args")[0])
                else:
                    conn = StdioConnectionParams(
                        server_params=StdioServerParameters(
                            command=server["command"],
                            args=server["args"]
                        ),
                        timeout=5
                    )
                toolset = MCPToolset(connection_params=conn)
                tools = await toolset.load_tools()
                tool_names = [tool.name for tool in tools]
                print(f"[bold green] Loaded tools from server [cyan]'{name}'[/cyan]: [/bold_green]{', '.join(tool_names)}")

                tools.append(toolset)
            except Exception as e:
                print(f"[bold red]Error loading tools from server (skipping)'{name}': {str(e)}[/bold_red]") 

        return tools

    def get_tools(self) -> list[MCPToolset]:
        """
        Returns the list of loaded MCPToolsets.
        """
        return self.tools.copy()