
import textwrap
from crewai import Task
from agents.research_specialist import research_specialist_agent

research_task = Task(
    agent=research_specialist_agent,
    description=textwrap.dedent("""
        Research the topic: {topic}

        Find up to 3 relevant sources using the search tool.

        Requirements:
        1. Prefer official documentation and reputable reports.
        2. Record the exact source title and original URL returned by search.
        3. Include statistics only when the search results explicitly support them.
        4. Never invent quotes, figures, reports, dates, or URLs.
        5. If a detail cannot be verified from the available results, say so.
        6. Prioritize relevant information published or updated in 2026.
        7. Record the publication or update date when available.
        8. Distinguish the publication date from the date of the data
           being reported.
        9. Open and verify original source pages when the available
           search tool and results permit it.
        10. Clearly label information as a verified historical fact,
            current measurement, estimate, or future forecast.
        11. Never describe a forecast as an actual measured result.
        12. If a source date or statistic cannot be verified, label it
            as unverified instead of guessing.
        13. Format monetary amounts clearly, for example:
            USD 7.84 billion or USD 52.62 billion.
        14. Preserve the original currency and units. Do not convert
            currencies unless specifically requested.
        15. If recent information is unavailable, state that clearly
            rather than presenting old information as new.

        Return a concise research summary with:
        - Main findings
        - Verified statistics, if available
        - Recent developments, if supported
        - Source publication dates, when available
        - Source titles and original URLs
        - Verification gaps and limitations

        Keep the summary under 500 words.
    """),
    expected_output=(
        "A concise research summary under 500 words. Include only "
        "supported findings, publication dates when available, clearly "
        "labelled facts and forecasts, verification limitations, and "
        "the exact source URLs returned by search."
    ),
    output_file="research_findings.md"
)
