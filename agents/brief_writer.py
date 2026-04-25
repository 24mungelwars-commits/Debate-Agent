from utils import call_llm

def brief_writer(topic: str, pro_data: dict, con_data: dict) -> str:
    prompt = f"""Write a structured debate brief for the topic: "{topic}"

PRO arguments:
{pro_data['arguments']}

CON arguments:
{con_data['arguments']}

Format exactly as:
## Topic
## Pro Side
(3 clear arguments with evidence)
## Con Side
(3 clear arguments with evidence)
## Key Clash Points
(2-3 areas where the two sides directly contradict each other)"""

    return call_llm(prompt)