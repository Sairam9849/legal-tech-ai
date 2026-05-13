from agno.agent import Agent
from tools.pdf_tool import extract_text_from_pdf

ingestion_agent = Agent(
    name="PDF Ingestion Agent",
    instructions="Extract text from PDF URL",
    tools=[extract_text_from_pdf]
)
