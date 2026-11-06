import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    params = StdioServerParameters(command="python", args=["clock_server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("tools:", [t.name for t in tools.tools])

            now = await session.call_tool("get_current_time", {})
            print("get_current_time() =", now.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())