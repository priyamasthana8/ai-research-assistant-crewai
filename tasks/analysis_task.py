
import textwrap
from crewai import Task
from agents.data_analyst import data_analyst_agent
from tasks.research_task import research_task

analysis_task = Task(
    agent=data_analyst_agent,
    description=textwrap.dedent("""
        Analyze the research on: {topic}

        Use only the findings provided by the research task.

        Requirements:
        1. Identify the 3 most important findings.
        2. Explain their practical implications.
        3. Separate supported facts from assumptions.
        4. Do not add outside facts or unsupported statistics.
        5. Preserve the source titles and URLs provided in the research.
        6. Mention gaps or limitations in the available evidence.
        7. Preserve source publication dates and data reference dates
           whenever they are provided.
        8. Clearly distinguish actual results, estimates, and forecasts.
        9. Do not describe projected future values as actual results.
        10. If sources disagree, explain the difference without treating
            different forecasts as directly comparable actual results.
        11. Use "USD X billion" formatting for dollar amounts.
        12. Do not claim a statistic is independently verified unless
            the research findings provide supporting evidence.
        13. If verification is incomplete, state that limitation clearly.

        Keep the analysis under 300 words.
    """),
    expected_output=(
        "An evidence-based analysis under 300 words, covering key findings, "
        "practical implications, limitations, original source URLs, "
        "publication dates when available, and clear distinctions between "
        "facts, estimates, and forecasts."
    ),
    context=[research_task],
    output_file="analysis_report.md"
)
