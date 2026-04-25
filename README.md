\# ⚖️ Debate Research Agent



An end-to-end AI agent system that researches both sides of any debate topic using 6 specialized agents, live web search, and an LLM-as-Judge evaluator.



Built for Semester IV B.E. ECE — Introduction to Agentic AI Systems.



🔗 \*\*Live Demo:\*\* \[https://debate-agent-ni72.onrender.com]



\---



\## What It Does



Enter any debate topic and the system:

1\. Searches the live web for pro and con arguments

2\. Validates source credibility

3\. Writes a structured debate brief

4\. Generates tactical rebuttals

5\. Scores the output using an LLM-as-Judge rubric



\---



\## Agent Pipeline



| Agent | Role |

|---|---|

| A1 — Pro Researcher | Searches live web for supporting arguments via Tavily |

| A2 — Con Researcher | Searches live web for opposing arguments via Tavily |

| A3 — Source Validator | Filters credibility, removes speculation and bias |

| A4 — Brief Writer | Structures a balanced, formatted debate brief |

| A5 — Rebuttal Agent | Generates tactical counter-arguments for both sides |

| A6 — Judge (LLM-as-Judge) | Scores output on 4-criterion rubric, gives feedback |



\---



\## Architecture



User Input (debate topic)

&#x20;     ↓

&#x20; Orchestrator

&#x20; ↙         ↘

A1 Pro      A2 Con

Researcher  Researcher

&#x20;  ↘         ↙

&#x20; (Tavily Search)

&#x20;     ↓

A3 Source Validator

&#x20;     ↓

A4 Brief Writer

&#x20;     ↓

A5 Rebuttal Agent

&#x20;     ↓

A6 Judge (LLM-as-Judge)

&#x20;     ↓

Debate Brief + Score



\---



\## Tech Stack



| Layer | Tool |

|---|---|

| Language | Python |

| UI | Streamlit |

| LLM | Groq (LLaMA 3.3 70B) |

| Search Tool | Tavily Search API |

| Deployment | Render |



\---



\## LLM-as-Judge Rubric



The Judge agent scores every output across 4 dimensions:



| Criterion | Description |

|---|---|

| Argument Strength | Are arguments logically sound? (1–10) |

| Evidence Quality | Are claims backed by credible sources? (1–10) |

| Balance | Does the brief fairly represent both sides? (1–10) |

| Rebuttal Quality | Are rebuttals specific and tactical? (1–10) |



\*\*Total: X / 40\*\* with actionable improvement suggestions.



\---



\## Project Structure



debate-agent/

├── app.py               # Streamlit UI

├── agents/

│   ├── pro\_researcher.py

│   ├── con\_researcher.py

│   ├── source\_validator.py

│   ├── brief\_writer.py

│   ├── rebuttal\_agent.py

│   └── judge.py

├── tools/

│   └── search.py        # Tavily wrapper

├── orchestrator.py

└── requirements.txt



\---



\## Run Locally



```bash

\# Clone the repo

git clone https://github.com/YOURUSERNAME/debate-agent.git

cd debate-agent



\# Create virtual environment

python -m venv venv

venv\\Scripts\\activate       # Windows

source venv/bin/activate    # Mac/Linux



\# Install dependencies

pip install -r requirements.txt



\# Add API keys

\# Create a .env file with:

\# GROQ\_API\_KEY=your\_key\_here

\# TAVILY\_API\_KEY=your\_key\_here



\# Run

streamlit run app.py

```



\---



\## Team



| Role | Responsibility |

|---|---|

| Architect \& Integrator | Problem definition, agent design, architecture, API integrations |

| Builder \& Deployer | Implementation, LLM-as-Judge, UI, deployment |



\---



\## Course



Introduction to Agentic AI Systems · Semester IV · B.E. Electronics \& Communication



