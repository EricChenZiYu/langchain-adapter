import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
llm = ChatOpenAI()

server_params = StdioServerParameters(
    command="python",
    # Make sure to update to the full absolute path to your math_server.py file
    args=["/Users/xingjiabin/Documents/dev_env/mcp/mcp_clients/langchain-adapter/servers/math_server.py"],
)


async def main():
    print("Hello from langchain-adapter!")
     


if __name__ == "__main__":
    asyncio.run(main())
