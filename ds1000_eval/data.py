import json
import random

def load_ds1000(dataset_path: str, library: str = "pandas"):
    """
    Load DS-1000 from JSONL or JSON and filter by metadata.library
    """
    data = []

    # Load jsonl
    if dataset_path.endswith(".jsonl"):
        with open(dataset_path, "r") as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
    else:  # load json
        with open(dataset_path, "r") as f:
            data = json.load(f)

    lib = library.lower()
    tasks = []

    for ex in data:
        meta_lib = ex.get("metadata", {}).get("library", "").lower()
        if meta_lib == lib:
            tasks.append(ex)

    random.shuffle(tasks)
    return tasks
