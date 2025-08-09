import os  

def gather_python_files(path="."):  
    script_list = []  
    for item in os.listdir(path):  
        if item.endswith(".py"):  
            script_list.append(item)  
    return script_list  

def run():  
    py_files = gather_python_files()  
    output_file = "Q1A.out"  

    with open(output_file, "w") as file:  
        for script in py_files:  
            file.write(script + "\n")  

if __name__ == "__main__":  
    run()
