from tools.tool_agent import run_tool
from providers.ollama_provider import ask_ollama
from memory.store import add_memory, get_recent_memory

print("Autonomous AI Agent started.")

while True:
    prompt = input("\nAsk the agent something: ")

    recent = get_recent_memory()

    if recent:
        context = "\n".join(
            [f"User: {m['prompt']}\nAgent: {m['response']}" for m in recent]
        )
        full_prompt = f"{context}\nUser: {prompt}"
    else:
        full_prompt = prompt

    # try tool execution first
    tool_result = run_tool(prompt)

    if tool_result == "No tool selected.":
        response = ask_ollama(full_prompt)
    else:
        response = tool_result

    print("\nAgent:", response)

    add_memory(prompt, response)
