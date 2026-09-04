import os
from functions.get_files_info import validate_path

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        path_is_valid, target_path = validate_path(working_directory, file_path)
        
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        if not path_is_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            # read the file
            MAX_CHARS = 10000
            with open(target_path, "r") as f:
                file_content = f.read(MAX_CHARS)
                if f.read(1):
                    file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content

    except:
        return f"Error: Something went wrong when trying to read the file"
