from providers.ollama_provider import ask_ollama
from tools.python_tool import run_python_code
import re


def extract_python(text: str) -> str:
    # look for python fenced block
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # look for generic fenced block
    match = re.search(r"```(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # fallback: return text itself
    return text.strip()


def solve_with_python(task: str) -> str:
    prompt = f"""
Write Python code that solves this task.

Rules:
Return ONLY Python code.
Do not include explanations.
The code must print the answer.

Task: {task}
"""

    raw = ask_ollama(prompt)

    code = extract_python(raw)

    return run_python_code(code)
