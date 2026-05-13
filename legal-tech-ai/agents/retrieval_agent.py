from agno.agent import Agent
from tools.embedding_tool import get_embedding

retrieval_agent = Agent(
    name="Retrieval Agent",
    instructions="Retrieve relevant chunks",
    tools=[get_embedding]
)
