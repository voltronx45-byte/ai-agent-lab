import json
import os

MEMORY_FILE = "memory/history.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def add_memory(prompt: str, response: str):
    history = load_memory()
    history.append({"prompt": prompt, "response": response})
    save_memory(history)

def get_recent_memory(limit: int = 3):
    history = load_memory()
    return history[-limit:]
