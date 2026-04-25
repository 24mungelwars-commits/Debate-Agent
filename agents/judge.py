from utils import call_llm

RUBRIC = {
    "argument_strength": "Are arguments logically sound with clear reasoning? (1-10)",
    "evidence_quality": "Are claims backed by credible, specific sources? (1-10)",
    "balance": "Does the brief fairly and completely represent both sides? (1-10)",
    "rebuttal_quality": "Are rebuttals specific, tactical, and well-targeted? (1-10)"
}

def judge(topic: str, brief: str, rebuttals: str) -> dict:
    rubric_text = "\n".join([f"- {k}: {v}" for k, v in RUBRIC.items()])

    prompt = f"""You are an expert debate judge. Evaluate this debate brief on: "{topic}"

RUBRIC (score each 1-10):
{rubric_text}

BRIEF:
{brief}

REBUTTALS:
{rebuttals}

Your response must follow this exact format:
**Argument Strength**: X/10 — [one sentence justification]
**Evidence Quality**: X/10 — [one sentence justification]
**Balance**: X/10 — [one sentence justification]
**Rebuttal Quality**: X/10 — [one sentence justification]

**Overall Score**: X/40

**Suggestions to improve**:
1. [specific suggestion]
2. [specific suggestion]"""

    return {"evaluation": call_llm(prompt), "rubric": RUBRIC}