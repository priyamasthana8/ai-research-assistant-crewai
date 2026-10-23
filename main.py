import os
import sys
import mcp.types

# MCP compatibility fix
class _FallbackMCPType:
    def __init__(self, *args, **kwargs):
        pass


_MCP_MISSING_TYPES = [
    "CacheableResult",
    "InputRequiredResult",
    "CallToolResult",
    "ContentBlock",
    "TextContent",
    "Tool",
]

for type_name in _MCP_MISSING_TYPES:
    if not hasattr(mcp.types, type_name):
        setattr(mcp.types, type_name, _FallbackMCPType)

# Groq prompt caching compatibility fix
try:
    import crewai.llms.cache as _crewai_cache
    _crewai_cache.mark_cache_breakpoint = lambda msg: msg
except (ImportError, AttributeError) as exc:
    print(f"Cache compatibility patch skipped: {exc}")

# Load environment variables before importing agents
from dotenv import load_dotenv
load_dotenv()

from crew import research_crew


def run(topic: str):
    result = research_crew.kickoff(inputs={"topic": topic})

    print("-" * 50)
    print(result)
    print("-" * 50)


if __name__ == "__main__":
    run("AI Agents")
