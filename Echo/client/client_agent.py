import asyncio
import sys
import os
import uuid
import httpx  # Ensure httpx is imported
sys.path.append("c:/Usha/UKRepos/A2AMaidan")

from common.client import A2AClient, A2ACardResolver
from common.types import TaskSendParams, Message, TextPart

async def query_agent(agent_url, user_text):
    # Fetch agent card automatically
    card_resolver = A2ACardResolver(agent_url)
    agent_card = card_resolver.get_agent_card()
    if not agent_card.skills:
        print("Warning: No skills provided in the agent card.")
        agent_card.skills = []  # Provide an empty list as a default
    if not agent_card.type:
        print("Warning: No type provided in the agent card.")
        agent_card.type = "unknown"  # Provide a default type
    # Print agent card details for debugging
    print("Discovered Agent:", agent_card.name)
    print("Agent Description:", agent_card.description)
    print("Agent URL:", agent_card.url)
    # Create A2A client with the correct task handling endpoint
    client = A2AClient(url="http://localhost:5001/tasks/send")  # Updated URL
    # Prepare Task parameters (using a plain dictionary to match the server's expected format)
    payload = {
        "id": str(uuid.uuid4()),  # Task ID
        "message": {
            "role": "user",
            "parts": [
                {"text": user_text}  # User's message
            ]
        }
    }
    # Send the task and wait for completion
    async with httpx.AsyncClient() as async_client:
        response = await async_client.post(client.url, json=payload)
        response.raise_for_status()
        result_task = response.json()
    # Extract agent's reply from result_task
    if result_task["status"]["state"] == "completed":
        # The A2A Task object can be inspected for messages and artifacts
        for msg in result_task["messages"]:
            if msg["role"] == "agent":
                # Print text parts of agent's message
                print("Agent's reply:", " ".join(part["text"] for part in msg["parts"] if "text" in part))

if __name__ == "__main__":
    agent_url = "http://127.0.0.1:5001"  # Updated to fetch the agent card
    user_text = "Hello, Agent!"  # Replace with the desired user input
    asyncio.run(query_agent(agent_url, user_text))