import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import argparse
from ds1000_eval.config import Config
from ds1000_eval.data import load_ds1000
from ds1000_eval.eval import run_task

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to DS-1000 JSON")
    parser.add_argument("--lib", type=str, default="pandas")
    parser.add_argument("--num", type=int, default=Config.NUM_TASKS)
    args = parser.parse_args()

    tasks = load_ds1000(args.data, args.lib)
    tasks = tasks[:args.num]

    print(f"Running {len(tasks)} DS-1000 tasks...\n")

    successes = 0
    for i, ex in enumerate(tasks):
        print(f"\n\n================= TASK {i+1} =================\n")
        if run_task(ex):
            successes += 1

    print("\n========================================")
    print(f"Success rate: {successes}/{len(tasks)} = {(successes/len(tasks))*100:.2f}%")
    print("========================================")

if __name__ == "__main__":
    main()

