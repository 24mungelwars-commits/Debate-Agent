from utils import call_llm

def source_validator(pro_data: dict, con_data: dict) -> dict:
    all_sources = pro_data["sources"] + con_data["sources"]
    sources_text = "\n".join([
        f"- {s['title']} ({s['url']}): {s['content'][:150]}"
        for s in all_sources
    ])

    prompt = f"""Review these sources and flag any that are:
- Opinion pieces without evidence
- Clearly biased or propaganda
- Speculative rather than factual

Sources:
{sources_text}

Return:
1) A list of credible sources with their URLs
2) A list of flagged sources with the reason for flagging"""

    return {"validation": call_llm(prompt), "verified_sources": all_sources}