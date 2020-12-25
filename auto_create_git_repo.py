import os
import subprocess
from github import Github

# personal token
# this is read from the .variables file
ACCESS_TOKEN = ''
# git url
GIT_URL = ''

def init_git_project():
    if os.path.exists('.git'):
        print("Git folder exists. Exit!")
        return

    # name of the project
    project_name = os.path.basename(os.getcwd())
    print(project_name)
            
    # description of the project
    description_value = "Auto sync repo for " + project_name
    print(description_value)
    
    # public or private project
    private_project = True;
    print("Private project will be made")
    
    # create git project
    create_git_project(project_name, description_value, private_project)

def read_variables():
    global ACCESS_TOKEN
    global GIT_URL    
    # get the location of the python file
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))    
    variables = {}
    with open(os.path.join(__location__, '.variables')) as f:
        for line in f:
            name, value = line.split('=')
            variables[name] = value.strip('\n')
            print(variables[name])

    ACCESS_TOKEN = variables['ACCESS_TOKEN']
    GIT_URL = variables['GIT_URL']    


def create_git_project(project_name, description_value, private_project):
    read_variables()
    # init git repo
    subprocess.run(["git", "init"], shell=True)
    # create readme.md
    # example is found here: https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
    if not os.path.exists('README.md'):
        with open("README.md","w") as f:
            f.write(f"# Project {project_name}\r\n")
            f.write("## Description \r\n")
            f.writelines(f"```{description_value}```")
    
    # ignore file
    # add here all files and folders you want to ignore
    if not os.path.exists('.gitignore'):
        print("Add .gitignore")
        # Add ignore
        with open(".gitignore","w") as f:
            f.write(".venv\r\n")
            f.write("node_modules\r\n")

    # add all files that there are in now
    subprocess.run(["git", "add", "."], shell=True)
    # commit the added files
    subprocess.run(["git", "commit", "-m", "Initial upload"], shell=True)

    # -------------------------------------------------------#
    # connect to git repository
    g = Github(ACCESS_TOKEN)
    # get current user object
    current_user = g.get_user()    
    # create new remote repository on git
    new_repo = current_user.create_repo(project_name, private=private_project, description=description_value)

    # -------------------------------------------------------#
    # add the remote repository
    subprocess.run(["git", "remote", "add", "origin", GIT_URL + new_repo.name], shell=True)
    # push the files to the remote git
    subprocess.run(["git", "push","--set-upstream","origin","master"], shell=True)

init_git_project()

