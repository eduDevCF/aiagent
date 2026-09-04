from functions.run_python_file import run_python_file

def test() -> None:
    # should print calculator's usage instrutions
    print(run_python_file("calculator", "main.py"))

    # should run the calculator with result 8
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # should run calculator's tests succesfully
    print(run_python_file("calculator", "tests.py"))

    # should return an error (out of working directory)
    print(run_python_file("calculator", "../main.py"))

    # should return an error (file does not exist)
    print(run_python_file("calculator", "nonexistent.py"))

    # should return an error (not a python file)
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    test()
