import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path
        results_header = format_results_header(directory)
        if not valid_target_dir:
            return f'{results_header}\n    Error: Cannot list "{directory}" as it is outside the permitted working directory.'
        if not os.path.isdir(target_dir):
            return f'    Error: "{directory}" is not a directory'
        if valid_target_dir:
            return results_header + format_results(target_dir, directory)
            # return f'Success: "{directory}" is within the working directory'
    except:
        return f"    Error: Something went wrong with directories"

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
            return f"{info_result}\nError: could not access info for '{file}' in {directory}' in '{target_dir}'"

    return file_info