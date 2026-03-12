from tools.python_tool import run_python_code
from tools.shell_tool import run_shell
from tools.file_tool import read_file, write_file

TOOLS = {
    "python": run_python_code,
    "shell": run_shell,
    "read_file": read_file,
    "write_file": write_file,
}
