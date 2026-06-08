import random
from fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Remote MCP Server")

# 1. Tool to add two numbers
@mcp.tool()
def add_two_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of the two numbers.
    """
    return a + b

# 2. Tool to generate a random number between 1 and 100
@mcp.tool()
def generate_random_number() -> int:
    """
    Generate a random integer between 1 and 100 (inclusive).
    
    Returns:
        A random integer between 1 and 100.
    """
    return random.randint(1, 100)

# 3. Resource to expose server_info
@mcp.resource("info://server_info")
def get_server_info() -> str:
    """
    Retrieve server metadata and configuration details.
    
    Returns:
        A string containing info about the server.
    """
    return (
        "Server Name: Remote MCP Server\n"
        "Version: 0.1.0\n"
        "Capabilities: Tools (add_two_numbers, generate_random_number), Resources (info://server_info)\n"
        "Status: Running\n"
        "Transport support: stdio, sse"
    )

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)
