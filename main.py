import tkinter as tk
from tkinter import filedialog
import os
import shutil
import subprocess

selected_directory = ""
project_name = "Project"

def select_directory():
    global selected_directory 
    initDir = os.path.expanduser('~/Documents')
    directory = filedialog.askdirectory(initialdir=initDir)
    if directory:
        selected_directory = directory
        print("Selected Directory:", selected_directory)
        skeleton(selected_directory)
    else:
        print("No Directory Selected")

import os
import shutil

import os
import shutil

def skeleton(directory):
    global project_name
    project_name = project.get()

    # Create directories
    os.mkdir(os.path.join(directory, project_name))
    os.mkdir(os.path.join(directory, project_name, 'HeaderFiles'))
    os.mkdir(os.path.join(directory, project_name, 'Resources'))
    os.mkdir(os.path.join(directory, project_name, 'LogicFiles'))
    shutil.copyfile('LogicFiles/Sample.cpp', os.path.join(directory, project_name, 'LogicFiles', 'Sample.cpp'))
    shutil.copyfile('HeaderFiles/Sample.h', os.path.join(directory, project_name, 'HeaderFiles', 'Sample.h'))
    shutil.copyfile('mainTemplate.cpp', os.path.join(directory, project_name, 'main.cpp'))
    root.destroy()


    command = f"cd {os.path.join(directory, project_name)} && code ."

    # Run the command in CMD
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
        # Check if the command was successful
        if result.returncode == 0:
            print("Command executed successfully.")
            print("Output:")
            print(result.stdout)
        else:
            print("Command failed.")
            print("Error:")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    # try:
    #     os.system(f"code .")
    # except Exception as e:
    #     print(f"Error opening VS Code: {str(e)}")

root = tk.Tk()
root.title("Directory Selection")
root.geometry('400x400')

project= tk.Entry(root)
project.pack(padx=20, pady=10)


select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

root.mainloop()

if selected_directory:
    print("Selected Directory (outside of tkinter):", selected_directory)
else:
    print("No Directory Selected (outside of tkinter)")
