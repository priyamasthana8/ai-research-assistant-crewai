import os
from crewai import Agent, LLM

llm = LLM(
    model=os.getenv("ANALYST_AGENT_LLM"),
    temperature=float(os.getenv("ANALYST_AGENT_TEMPERATURE")),
    api_key=os.getenv("GROQ_API_KEY")
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Extract useful insights from the provided research without adding unsupported claims.",
    backstory=(
        "You analyze research carefully, identify important patterns, "
        "and explain their practical significance. You do not invent "
        "statistics or introduce facts that are absent from the research. "
        "You preserve source titles and original URLs."
    ),
    llm=llm,
    verbose=True,
    max_iter=2,
    allow_delegation=False
)
