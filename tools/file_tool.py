import os

def read_file(path: str) -> str:
    if not os.path.exists(path):
        return f"File not found: {path}"

    with open(path, "r") as f:
        return f.read()

def write_file(path: str, content: str) -> str:
    with open(path, "w") as f:
        f.write(content)

    return f"File written: {path}"
