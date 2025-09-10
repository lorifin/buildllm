#from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.run_python_file import run_python_file
def main():
    working_directory = "calculator"
    #result = write_file(working_directory, "lorem.txt", "wait, this isn't lorem ipsum")
    
    #print(result)
    print(run_python_file(working_directory, "main.py", ["3 + 5"]))
    

main ()
