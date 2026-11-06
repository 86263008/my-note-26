from datetime import datetime

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("clock")


@mcp.tool()
def get_current_time() -> str:
    """返回当前的真实系统时间，格式为 YYYY-MM-DD HH:MM:SS。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    mcp.run()