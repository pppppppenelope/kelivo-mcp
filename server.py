from fastmcp import FastMCP

mcp = FastMCP("Narrative Storage Server")

@mcp.tool()
def store_narrative(content: str) -> str:
    """将角色扮演的完整正文存入此工具，原样返回以展示给用户。"""
    return content

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)
