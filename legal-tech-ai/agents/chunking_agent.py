from agno.agent import Agent

def chunk_text(text, size=500):
    return [text[i:i+size] for i in range(0, len(text), size)]

chunking_agent = Agent(
    name="Chunking Agent",
    instructions="Split text into chunks",
    tools=[chunk_text]
)
