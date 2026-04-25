from tools.search import search
from utils import call_llm

def pro_researcher(topic: str) -> dict:
    results = search(f"arguments in favor of {topic}")
    sources_text = "\n".join([f"- {r['title']}: {r['content'][:200]}" for r in results])

    prompt = f"""You are a debate researcher. Based on these search results,
extract the 3 strongest PRO arguments for: "{topic}"

Sources:
{sources_text}

Format your response as a numbered list with a clear argument title and 2-sentence explanation each."""

    return {"arguments": call_llm(prompt), "sources": results}