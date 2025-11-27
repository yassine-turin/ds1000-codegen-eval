import json
import random

def load_ds1000(dataset_path: str, library: str = "pandas"):
    """
    Load a subset of DS-1000 filtered by library tag.
    """
    with open(dataset_path, "r") as f:
        data = json.load(f)

    tasks = [ex for ex in data if library.lower() in ex.get("libraries", [])]
    random.shuffle(tasks)
    return tasks

