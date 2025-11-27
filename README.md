# ds1000-codegen-eval

A simple evaluator for testing an LLM (e.g., OpenAI GPT models) on a subset of the **DS-1000** dataset.  
The model generates Python code for each task, the code is cleaned and executed, and a success rate is reported.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
