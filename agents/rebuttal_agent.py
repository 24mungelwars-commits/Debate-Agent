from utils import call_llm

def rebuttal_agent(topic: str, pro_args: str, con_args: str) -> str:
    prompt = f"""For the debate topic: "{topic}"

Generate sharp, specific rebuttals:

1. How the PRO side would rebut each CON argument
2. How the CON side would rebut each PRO argument

PRO arguments:
{pro_args}

CON arguments:
{con_args}

Be tactical and specific. Reference the actual arguments, not generic responses."""

    return call_llm(prompt)