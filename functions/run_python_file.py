import os
import subprocess
from google.genai import types
def run_python_file(working_directory: str, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(
                final_args,
                capture_output=True,
                text=True,
                cwd=working_directory,
                timeout=30,
            )
            
        final_string =f"""
        stdout: {output.stdout}
        stderr: {output.stderr}
        """
        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced"
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
        
        return final_string
    except Exception as e:
        return f"Error running python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with the python interpreter. Accepts additional CLI args as an optional array  constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run,relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
            ),               
        },
    ),
)