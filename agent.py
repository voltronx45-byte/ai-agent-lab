import ollama

print("Local AI Agent started.")

while True:
    prompt = input("\nAsk the agent something: ")

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nAgent:", response["message"]["content"])

