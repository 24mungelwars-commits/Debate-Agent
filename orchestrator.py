from agents.pro_researcher import pro_researcher
from agents.con_researcher import con_researcher
from agents.source_validator import source_validator
from agents.brief_writer import brief_writer
from agents.rebuttal_agent import rebuttal_agent
from agents.judge import judge

def run_debate_agent(topic: str, status_callback=None) -> dict:

    def update(msg):
        if status_callback:
            status_callback(msg)

    update("A1 — Pro Researcher searching...")
    pro_data = pro_researcher(topic)

    update("A2 — Con Researcher searching...")
    con_data = con_researcher(topic)

    update("A3 — Source Validator checking credibility...")
    validated = source_validator(pro_data, con_data)

    update("A4 — Brief Writer structuring arguments...")
    brief = brief_writer(topic, pro_data, con_data)

    update("A5 — Rebuttal Agent generating counter-arguments...")
    rebuttals = rebuttal_agent(topic, pro_data["arguments"], con_data["arguments"])

    update("A6 — Judge evaluating quality...")
    judgment = judge(topic, brief, rebuttals)

    return {
        "topic": topic,
        "pro": pro_data["arguments"],
        "con": con_data["arguments"],
        "sources": validated["validation"],
        "brief": brief,
        "rebuttals": rebuttals,
        "judgment": judgment["evaluation"]
    }