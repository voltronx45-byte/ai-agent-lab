from providers.ollama_provider import ask_ollama
from providers.openai_provider import ask_openai
from tools.python_tool import run_python_code
from tools.task_python_tool import solve_with_python
from tools.file_tool import read_file, write_file
from tools.shell_tool import run_shell


def route_prompt(prompt: str) -> str:
    lower_prompt = prompt.lower().strip()

    if lower_prompt.startswith("solve with python:"):
        task = prompt.split(":", 1)[1].strip()
        return solve_with_python(task)

    if lower_prompt.startswith("python:"):
        code = prompt.split(":", 1)[1].strip()
        return run_python_code(code)

    if lower_prompt.startswith("shell:"):
        command = prompt.split(":", 1)[1].strip()
        return run_shell(command)

    if lower_prompt.startswith("read file:"):
        path = prompt.split(":", 1)[1].strip()
        return read_file(path)

    if lower_prompt.startswith("write file:"):
        parts = prompt.split(":", 2)
        if len(parts) < 3:
            return "Usage: write file: filename : content"
        path = parts[1].strip()
        content = parts[2].strip()
        return write_file(path, content)

    if lower_prompt.startswith("code:"):
        clean_prompt = prompt.split(":", 1)[1].strip()
        return ask_openai(clean_prompt)

    if lower_prompt.startswith("local:"):
        clean_prompt = prompt.split(":", 1)[1].strip()
        return ask_ollama(clean_prompt)

    return ask_ollama(prompt)
