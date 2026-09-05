import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        results_header = format_results_header(directory)
        
        path_is_valid, target_dir = validate_path(working_directory, directory)
        
        if not os.path.isdir(target_dir):
            return f'    Error: "{directory}" is not a directory'
        if not path_is_valid:
            return f'{results_header}\n    Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        else:
            return results_header + format_results(target_dir, directory)
            # return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"    Error: Something went wrong when trying to list these files: {e}"


def validate_path(working_directory: str, target_dir: str) -> (bool, str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.normpath(os.path.join(abs_working_dir, target_dir))
    is_valid = os.path.commonpath([abs_working_dir, abs_target_dir]) == abs_working_dir
    return is_valid, abs_target_dir


def format_results_header(directory: str) -> str:
    info_result = "Result for "
    if directory == ".":
        info_result += "current "
    else:
        info_result += f"'{directory}' "
    info_result += "directory:"
    return info_result


def format_results(target_dir: str, directory: str) -> str:
    files: str = os.listdir(target_dir)
    file_info: str = ""
    for file in files:
        try:
            if file.startswith("__") and file.endswith("__"):
                continue
            file_abs_path = os.path.normpath(os.path.join(target_dir, file))
            file_size = os.path.getsize(file_abs_path)
            is_dir = os.path.isdir(file_abs_path)
            file_info += f"\n  - {file}: file_size={file_size} bytes, is_dir={is_dir}"
        except:
            return f"\nError: could not access info for '{file}' in {directory}' in '{target_dir}'"

    return file_info