import os  # <--- 新增这一行
from fastmcp import FastMCP

mcp = FastMCP("Narrative Storage Server")

@mcp.tool()
def store_narrative(content: str) -> str:
    """将角色扮演的完整正文存入此工具，原样返回以展示给用户。"""
    return content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) # <--- 改成这一行，让它自动识别端口
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
