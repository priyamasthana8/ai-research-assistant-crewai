import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

llm = LLM(
    model=os.getenv("RESEARCH_AGENT_LLM"),
    temperature=float(os.getenv("RESEARCH_AGENT_TEMPERATURE")),
    api_key=os.getenv("GROQ_API_KEY")
)

research_specialist_agent = Agent(
    role="Research Specialist",
    goal="Find reliable evidence and preserve original source URLs.",
    backstory=(
        "You are a careful research specialist. You distinguish verified "
        "information from assumptions. You never fabricate statistics, "
        "quotes, source titles, or URLs. You use search results honestly "
        "and report when evidence is insufficient."
    ),
    llm=llm,
    tools=[SerperDevTool(n_results=3)],
    verbose=True,
    max_iter=3,
    allow_delegation=False
)
