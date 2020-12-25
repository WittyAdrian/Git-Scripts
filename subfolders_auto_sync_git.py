import os
import subprocess
import glob
import shutil
from github import Github

# personal token
# this is read from the .variables file
ACCESS_TOKEN = ''
# git url
GIT_URL = ''

def loop_through_subfolders():
    for folder in os.listdir("."):
        print('\n=========================\n >>> {} <<< \n=========================\n'.format(folder))
        sync_git_project(folder)

def read_variables():
    global ACCESS_TOKEN
    global GIT_URL    
    # get the location of the python file
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))    
    variables = {}
    with open(os.path.join(__location__, '.variables')) as f:
        for line in f:
            name, value = line.split('=')
            variables[name] = value.strip('\n')
            print(variables[name])

    ACCESS_TOKEN = variables['ACCESS_TOKEN']
    GIT_URL = variables['GIT_URL']    

def sync_git_project(folder_name):
    print('Starting AutoSync...')
    read_variables()
        
    # add all files that there are in now
    subprocess.run(["git", "add", "."], shell=True, cwd=folder_name)
    # commit the added files
    subprocess.run(["git", "commit", "-m", "AutoSync for {}".format(datetime.now())], shell=True, cwd=folder_name)
    # push the files to the remote git
    subprocess.run(["git", "push"], shell=True, cwd=folder_name)