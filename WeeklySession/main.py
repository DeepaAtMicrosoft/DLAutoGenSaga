
import asyncio
import os
from dotenv import load_dotenv
from colorama import Fore
from autogen_agentchat.agents import AssistantAgent # type: ignore
from autogen_agentchat.ui import Console # type: ignore
from autogen_ext.models.openai import OpenAIChatCompletionClient # type: ignore
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient # type: ignore
from autogen_agentchat.teams import DiGraphBuilder, GraphFlow

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

IDEAPROMPT = "You are a creative idea generating assistant who generates and explains product ideas clearly in 1 sentence."
PITCHPROMPT="You are a creative idea pitching assistant who creates engaging pitches for product ideas in 100 words.  Use the idea created by idea agent and then crete pitch on that.  Use colors and emojis to make it more engaging."
# 1. Set up OpenAI model client
# Create an agent that uses the OpenAI GPT-4o model.
model_client = OpenAIChatCompletionClient(
    model="gpt-3.5-turbo",  
    api_key=OPENAI_API_KEY,
)

azuremodel_client = AzureOpenAIChatCompletionClient(
    api_key=OPENAI_API_KEY,
    azure_deployment="gpt-4.1",
    api_version="2025-01-01-preview",
    model="gpt-4.1",
    azure_endpoint="https://autogendlsaga.openai.azure.com/",
)

# 2. Set up Single Agent (AssistantAgent)
ideaagent = AssistantAgent(
    name="idea_generator_agent",
    model_client=model_client,
    system_message=IDEAPROMPT,
)

pitchAgent=AssistantAgent(
    name="idea_pitch_agent",
    model_client=model_client,
    system_message=PITCHPROMPT,
)


builder=DiGraphBuilder()
builder.add_node(ideaagent)
builder.add_node(pitchAgent)
builder.add_edge(ideaagent,pitchAgent)
builder.set_entry_point(ideaagent)
graph=builder.build()

flow=GraphFlow([ideaagent,pitchAgent],graph)

# Async function for getting results
async def main():
    # await Console(ideaagent.run_stream(task="Create a marketing concept for an 'idea box'"))
    # await Console(pitchAgent.run_stream(task="Create a pitch for the product idea created by idea agent"))
    await Console(flow.run_stream(task="Create a product idea for an idea box"))
    await model_client.close()


# Entry point
if __name__ == "__main__":
    asyncio.run(main())

