import subprocess
import tempfile
import os

def run_python_code(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        temp_path = f.name

    try:
        result = subprocess.run(
            ["python3", temp_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            return result.stdout.strip() or "Code ran successfully with no output."
        return result.stderr.strip() or "Python code failed."
    except Exception as e:
        return f"Python tool error: {e}"
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
