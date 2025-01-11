from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os

# Установите API-ключи
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"

async def main():
    llm = ChatOpenAI(model="gpt-4o")
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
