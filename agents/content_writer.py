import os
from crewai import Agent, LLM

llm = LLM(
    model=os.getenv("WRITER_AGENT_LLM"),
    temperature=float(os.getenv("WRITER_AGENT_TEMPERATURE")),
    api_key=os.getenv("GROQ_API_KEY")
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Write a concise, factual report based only on the supplied analysis.",
    backstory=(
        "You write clear, structured reports. You never fabricate facts, "
        "statistics, quotations, citations, or URLs. You preserve the "
        "provided source links and clearly disclose evidence limitations."
    ),
    llm=llm,
    verbose=True,
    max_iter=2,
    allow_delegation=False
)
