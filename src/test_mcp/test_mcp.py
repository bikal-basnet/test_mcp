# main.py
from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP("Demo MCP Server")


@mcp.tool(description="Say Hi.")
def say_hi() -> TextContent:
    return TextContent(type="text", text="Hi how are you")


# def main():
#     print("Starting MCP server")
#     mcp.run()


# if __name__ == "__main__":
#     main()
