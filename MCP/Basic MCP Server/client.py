import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters,stdio_client

server = StdioServerParameters(
    command="python",
    args=["server.py"]
)

async def connect_mcp():
    async with stdio_client(server) as (read,write):
        async with ClientSession(read,write) as session:

            # Initialize MCP connection
            await session.initialize()

            # Get available tools
            tools = await session.list_tools()

            for tool in tools.tools:
                print("Tool Name:", tool.name)
                print("Tool Description:", tool.description)
                print("Tool Arguments:", tool.inputSchema)

            # Call AddNumbers tool
            result = await session.call_tool("AddNumbers",{"a": 20, "b": 30})
            print("Tool Result:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(connect_mcp())