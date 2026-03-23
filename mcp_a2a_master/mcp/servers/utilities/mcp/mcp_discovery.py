import os
import json
from typing import Dict, Any

class MCPDiscovery:
    """
    Reads a JSON config file defining MCP servers and provides access to server definitions under the mcpServers key
    
    Attributes:
        congig_file (str): The path to the JSON config file
        config (Dict[str, Any]): Parsed JSON content, expected to contain an "mcpServers" key with server definitions
        """
    def __init__(self, config_file: str):
        """
        Initializes the MCPDiscovery instance by reading and parsing the specified JSON config file.
        Args:
            config_file (str, optional): The path to the JSON config file, If none, defaults to "mcp_config.json" 
            located in the same directory as this module.
        """
        if config_file is None:
            config_file = os.path.join(
                os.path.dirname(__file__), 
                "mcp_config.json")
        else:
            self.config_file = config_file

        self.config = self._load_config()

    def _load_config(self) -> Dict(str, Any): # type: ignore
        """
        Loads and parses the JSON config file.
        Returns:
        Dict[str, Any]: The parsed JSON content of the config file.
        """
        try:
            with open(self.config_file, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict) or "mcpServers" not in data:
                raise ValueError(f"Invalif config format in {self.config_file}")
            
            return data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"config file {self.config_file} not found.")
        
        except Exception as e:
            return RuntimeError(f"Error loading config file {self.config_file}: {str(e)}")
        
    def list_servers(self) -> Dict[str, Any]:
        """
        Returns the server definitions under the "mcpServers" key in the config.

        Returns:
            Dict[str, Any]: The content of the "mcpServers" key from the config.

        Raises:
            KeyError: If the "mcpServers" key is not found in the config.
        """

        if "mcpServers" not in self.config:
            raise KeyError(f"'mcpServers' key not found in config file {self.config_file}")
        return self.config.get("mcpServers", {})
        
