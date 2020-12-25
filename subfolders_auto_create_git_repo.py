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
        init_git_project(folder)

def init_git_project(folder_name):
    if os.path.exists('{}/.git'.format(folder_name)):
        print("Git folder exists. Exit!")
        return

    # name of the project
    project_name = folder_name
    print(project_name)
            
    # description of the project
    description_value = "Auto sync repo for " + project_name
    print(description_value)
    
    # public or private project
    private_project = True;
    print("Private project will be made")
    
    # create git project
    create_git_project(project_name, description_value, private_project, folder_name)

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

def copy_gitignore_file(filename):
    print("Copying {} git ignore file...".format(filename.upper()))
    sourcePath = "{}\\{}}.gitignore".format(os.path.dirname(os.path.realpath(__file__)), filename)
    targetPath = "{}\\.gitignore".format(folder_name)
    print("Copying from [{}] to [{}]".format(sourcePath, targetPath))
    shutil.copyfile(sourcePath, targetPath)

def create_git_project(project_name, description_value, private_project, folder_name):
    read_variables()
    # init git repo
    subprocess.run(["git", "init"], shell=True, cwd=folder_name)
    # create readme.md
    # example is found here: https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
    if not os.path.exists('{}\\README.md'.format(folder_name)):
        with open('{}\\README.md'.format(folder_name),"w") as f:
            f.write(f"# Project {project_name}\r\n")
            f.write("## Description \r\n")
            f.writelines(f"```{description_value}```")
    
    # ignore file
    # add here all files and folders you want to ignore
    if not os.path.exists('.gitignore'):
        print("Add .gitignore")
        # Add ignore
        if (os.path.exists("{}/ProjectSettings".format(folder_name))):
            copy_gitignore_file('unity')
        elif (glob.glob("{}/*.sln".format(folder_name))):
            copy_gitignore_file('csharp')

    # add all files that there are in now
    subprocess.run(["git", "add", "."], shell=True, cwd=folder_name)
    # commit the added files
    subprocess.run(["git", "commit", "-m", "Initial upload"], shell=True, cwd=folder_name)

    # -------------------------------------------------------#
    # connect to git repository
    g = Github(ACCESS_TOKEN)
    # get current user object
    current_user = g.get_user()    
    # create new remote repository on git
    new_repo = current_user.create_repo(project_name, private=private_project, description=description_value)

    # -------------------------------------------------------#
    # add the remote repository
    subprocess.run(["git", "remote", "add", "origin", GIT_URL + new_repo.name], shell=True, cwd=folder_name)
    # push the files to the remote git
    subprocess.run(["git", "push","--set-upstream","origin","master"], shell=True, cwd=folder_name)

loop_through_subfolders()

