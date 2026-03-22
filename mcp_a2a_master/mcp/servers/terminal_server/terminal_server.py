from mcp.server.fastmcp import FastMCP
import os
import subprocess

mcp = FastMCP("terminal_server")
DEFAULT_WORKSPACE = os.path.expanduser("~/Desktop/Projects/MCP_Server/workspace") #location where agent will save new/edited files
os.makedirs(DEFAULT_WORKSPACE, exist_ok=True) 

# define a tool
@mcp.tool("terminal_server_tool")
async def run_command(command: str) -> str:
    """
    Run a terminal command and return the output.
    Args:
        command (str): The terminal command to run.
    Returns:
        str: The output of the command or an error message if it fails.
    """
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd = DEFAULT_WORKSPACE, 
            stdout=subprocess.PIPE,  
            stderr=subprocess.PIPE, 
            text=True)
        return result.stdout or result.stderr or "Command finished with no output."
    except Exception as e:
        return f"Error running command: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")