import os
from functions.get_files_info import validate_path
from config import MAX_CHARS

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Open a file given its path and read and return the text",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the file to be read within the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str, no_max: bool=False) -> str:
    try:
        path_is_valid, target_path = validate_path(working_directory, file_path)
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if not path_is_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            # fetch with no_max for logging only
            if no_max:
                with open(target_path, "r") as l:
                    past_logs = l.read()
                return past_logs
            # read the file
            with open(target_path, "r") as f:
                file_content = f.read(MAX_CHARS)
                if f.read(1):
                    file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content

    except Exception as e:
        return f"Error: Something went wrong when trying to read the file at '{file_path}': {e}"
