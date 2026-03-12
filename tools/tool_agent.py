from providers.ollama_provider import ask_ollama
from tools.registry import TOOLS


def normalize_tool_name(name: str) -> str:
    name = name.strip()
    if "(" in name:
        name = name.split("(", 1)[0].strip()
    return name


def choose_tool(prompt: str) -> str:
    tool_prompt = f"""
You are an AI agent that can use tools.

Available tools:
python(code)
shell(command)
read_file(path)
write_file(path, content)

Respond with ONLY one line in this exact format:

tool_name: argument

Examples:
shell: ls
python: print("hello")
read_file: agent.py
write_file: notes.txt : hello world

User request:
{prompt}
""".strip()

    decision = ask_ollama(tool_prompt).strip()
    return decision


def run_tool(prompt: str) -> str:
    decision = choose_tool(prompt)

    if ":" not in decision:
        return "No tool selected."

    tool_name, arg = decision.split(":", 1)

    tool_name = normalize_tool_name(tool_name)
    arg = arg.strip()

    if tool_name not in TOOLS:
        return f"Unknown tool: {tool_name}"

    return TOOLS[tool_name](arg)
