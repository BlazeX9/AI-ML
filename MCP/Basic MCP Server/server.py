from mcp.server.fastmcp import FastMCP
mcp = FastMCP("MCP Server")

@mcp.tool("AddNumbers")
def add_numbers(a: int, b: int) -> str:
    """Add two numbers."""
    return f"Sum = {a + b}"

@mcp.tool("MultiplyNumbers")
def multiply_numbers(a: int, b: int) -> str:
    """Multiply two numbers."""
    return f"Product = {a * b}"

if __name__ == "__main__":
    print("MCP server is running...")
    mcp.run()