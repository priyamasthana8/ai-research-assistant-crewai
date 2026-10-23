
import textwrap
from crewai import Task
from agents.content_writer import content_writer_agent
from tasks.analysis_task import analysis_task

writing_task = Task(
    agent=content_writer_agent,
    description=textwrap.dedent("""
        Write a factual report on: {topic}

        Use only the evidence and source URLs in the analysis provided.

        Rules:
        1. Do not invent statistics, quotes, source names, or URLs.
        2. Do not present assumptions as verified facts.
        3. If evidence is insufficient, state that clearly.
        4. Keep the report concise and avoid repetition.
        5. Preserve source publication dates and data reference dates
           when provided in the analysis.
        6. Clearly distinguish actual measurements, estimates, and
           future forecasts.
        7. Never present a forecast as an actual result.
        8. Preserve the original currency and units.
        9. Format monetary values as "USD 7.84 billion" instead of
           ambiguous or incorrectly formatted dollar symbols.
        10. Preserve source titles and URLs exactly as provided.
        11. Do not claim that a source was independently verified if
            the analysis does not establish that verification.
        12. Mention when source dates, statistics, or evidence could
            not be verified.

        Use these sections:
        1. Executive Summary
        2. Key Findings
        3. Analysis and Recommendations
        4. Limitations
        5. Sources

        In Sources, preserve the exact source titles and original URLs
        provided in the analysis.

        Keep the report between 250 and 350 words.
    """),
    expected_output=(
        "A factual report between 250 and 350 words with all five required "
        "sections, source URLs preserved from the analysis, clear date "
        "references, properly formatted currency values, and distinctions "
        "between verified facts, estimates, and forecasts."
    ),
    context=[analysis_task],
    output_file="final_report.md"
)
