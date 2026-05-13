from agents.ingestion_agent import ingestion_agent

pdf_url = "YOUR_PDF_URL"

text = ingestion_agent.run(pdf_url)
print(text)
