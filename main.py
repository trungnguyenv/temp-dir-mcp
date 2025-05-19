# server.py
from mcp.server.fastmcp import FastMCP
import tempfile
import os

# Create an MCP server
mcp = FastMCP("A toolkit to provide a temporary working directory for AI Agents")

DIR = "/Users/trungnguyen/Workspace/Vibe-Testing/tmp"

# Add an addition tool
@mcp.tool()
def get_working_directory() -> str:
    """Get a temporary working directory"""
    return DIR

# @mcp.tool()
def clean_working_directory() -> str:
    """Clean the temporary working directory completely"""
    
    for item in os.listdir(DIR):
        item_path = os.path.join(DIR, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            import shutil
            shutil.rmtree(item_path)
    return f"Cleaned all files and folders in {DIR}"

@mcp.tool()
def clean_working_directory_except(exclude: list[str]) -> str:
    """Clean the temporary working directory except specified files/folders
    
    Args:
        exclude: List of file/folder names to preserve
    """
    
    for item in os.listdir(DIR):
        if item in exclude:
            continue
        item_path = os.path.join(DIR, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            import shutil
            shutil.rmtree(item_path)
    return f"Cleaned all files and folders in {DIR} except {exclude}"

# Start the server
if __name__ == "__main__":
    mcp.run()
