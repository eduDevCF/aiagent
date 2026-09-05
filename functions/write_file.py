import os
from functions.get_files_info import validate_path
from functions.get_file_content import get_file_content

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write provided text to a specified file path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "A file path to write to within the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The text to write to the file",
                },
            "required": ["file_path", "content"],
            },
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        path_is_valid, target_path = validate_path(working_directory, file_path)
        
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        if not path_is_valid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        else:
            # make all parent directories if they don't exist
            os.makedirs(os.path.dirname(target_path), exist_ok=True)

            # write to file path
            with open(target_path, "w") as f:
                f.write(content)
            
            # read file to check if it wrote all the content
            try:
                written_content = get_file_content(working_directory, target_path)
                if len(written_content) == len(content):
                    return f'Successfully wrote to "{target_path}" ({len(content)} characters written)'
            except Exception as e:
                return f"Error: Something went wrong when confirming that we wrote to the file: {e}"
    except Exception as e:
        return f"Error: Something went wrong trying to write to '{file_path}': {e}"