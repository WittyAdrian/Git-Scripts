import os
import subprocess
import glob
import shutil
from datetime import datetime

def list_all_folders():
    index = 1
    for folder in os.listdir("."):
        if (os.path.exists("{}/ProjectSettings".format(folder))):
            print("[UNITY] {}) {}".format(index, folder))
        elif (glob.glob("{}/*.sln".format(folder))):
            print("[C#] {}) {}".format(index, folder))
        else:
            print("_______ {}) {}".format(index, folder))

        index += 1
    
def copy_file_with_namechange():    
    sourcePath = "{}\\test.txt".format(os.path.dirname(os.path.realpath(__file__)))
    targetPath = "targettest.txt"
    print("Copying from [{}] to [{}]".format(sourcePath, targetPath))
    shutil.copyfile(sourcePath, targetPath)

def run_subprocess_on_subfolder():
    subprocess.Popen(["dir"], shell=True, cwd='StreamDeck')
    
def check_for_git_changes():
    print("TO DO")

def get_current_datetime():
    print(datetime.now())
    print(datetime.date(datetime.now()))
    print(datetime.time(datetime.now()))

print(" === DEBUG STARTING === \n")

# list_all_folders()
# get_current_datetime()
# copy_file_with_namechange()
run_subprocess_on_subfolder()

print("\n === DEBUG FINISHED === ")