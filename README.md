# ds1000-codegen-eval

This repo evaluates a hosted LLM (e.g. OpenAI `gpt-4.1-mini`) on a subset of
the **DS-1000** dataset, focusing on a specific library (e.g. `Pandas`).

For each task:

1. Take the natural-language problem description (`prompt`).
2. Ask the LLM to generate Python code that solves it.
3. Clean the model output (strip ``` fences, `<code>` tags, etc.).
4. Execute the code in a sandboxed environment.
5. Check whether it runs and produces a `result` variable.
6. Compute a simple success rate across tasks.

> This is **evaluation**, not training. The model is not updated or fine-tuned;
> we just measure how often it can solve DS-1000 problems.

---

## Setup

### 1. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
