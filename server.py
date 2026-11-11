import os, requests
from fastmcp import FastMCP

mcp = FastMCP("s")
KEY = os.environ.get("DEEPSEEK_API_KEY", "")

@mcp.tool
def search(q: str) -> str:
    """搜索网页"""
    r = requests.post("https://api.deepseek.com/v1/tools/search",
        headers={"Authorization": f"Bearer {KEY}"},
        json={"query": q, "count": 8}, timeout=30)
    return str(r.json().get("results", []))

@mcp.tool
def fetch(url: str) -> str:
    """读网页"""
    r = requests.post("https://api.deepseek.com/v1/tools/fetch",
        headers={"Authorization": f"Bearer {KEY}"},
        json={"url": url}, timeout=60)
    return r.json().get("content", "")[:6000]

if __name__ == "__main__":
    mcp.run()
