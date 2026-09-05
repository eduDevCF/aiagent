import os, subprocess
from functions.get_files_info import validate_path

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a python file given a file path and a list of args as a subprocess",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the Python file to be run",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "To call a function with arguments, pass them as an array whose items are strings. The default is an empty array: []"
                },
                "required": ["file_path"],
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list=[]) -> str:
    try:
        path_is_valid, abs_path = validate_path(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)

        if not os.path.isfile(abs_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        if not path_is_valid:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            # build the command
            command = ["python", abs_path]
            if args:
                command.extend(args)
            # run the command in a subprocess
            completed_process = subprocess.run(
                command, 
                cwd=abs_working_dir,
                capture_output=True, 
                text=True, 
                timeout=30)
            # build output string
            output = ""
            if completed_process.returncode != 0:
                output += f"Error: Process exited with code {completed_process.returncode}\n"
            if not completed_process.stdout and not completed_process.stderr:
                output += "No output produced\n"
            if completed_process.stdout:
                output += f"STDOUT: {completed_process.stdout}\n"
            if completed_process.stderr:
                output += f"STDERR: {completed_process.stderr}\n"
            return output

    except Exception as e:
        return f"Error: Something went wrong executing Python file '{file_path}': {e}"
