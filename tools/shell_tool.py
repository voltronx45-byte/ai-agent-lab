import subprocess

def run_shell(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode == 0:
            return result.stdout.strip() or "Command ran successfully."
        return result.stderr.strip()

    except Exception as e:
        return f"Shell error: {e}"
