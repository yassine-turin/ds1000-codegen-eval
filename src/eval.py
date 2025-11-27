import traceback
import textwrap
from src.llm import generate_code
from src.cleaning import clean_code

def run_task(example: dict) -> bool:
    prompt = example["prompt"]

    print("=== PROBLEM ===")
    print(textwrap.shorten(prompt, width=250))

    # Call LLM
    raw = generate_code(prompt)

    print("\n=== RAW MODEL OUTPUT ===")
    print(raw)

    code = clean_code(raw)

    print("\n=== CLEANED CODE ===")
    print(code)

    # Execute
    local_vars = {}

    try:
        exec(code, {}, local_vars)

        if "result" in local_vars:
            print("\nExecution OK, `result` found.")
            return True
        else:
            print("\nExecution OK, but no variable `result` was defined.")
            return False

    except Exception:
        print("\nExecution FAILED:")
        print(traceback.format_exc())
        return False
