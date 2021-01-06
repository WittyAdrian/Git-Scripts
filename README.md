# Project Git Scripts

```Auto sync repo for Git Scripts```

## Description 

Collection of Python scripts to generate GIT repositories and automatically synchronize data to them.

To create a new repository:
 - `create_git_repo.py`: Manually enter info and create a new repository in the current folder
 - `auto_create_git_repo.py`: Automatically create a new repository in the current folder
 - `subfolders_auto_create_git_repo.py`: Automatically create new repositories in each subfolder
 
Premade gitignore files to be used in the `auto` scripts:
 - `csharp_gitignore`: Ignore file for a regular C# project
 - `unity.gitignore`: Ignore file for a Unity project
 
To synchronize data in an existing repository:
 - `subfolders_auto_sync_git.py`: Synchronize the repository in each subfolder
 
In order to schedule the sync automatically:
 - `run_auto_sync.bat`: Use Windows Task Scheduler to create automatic syncing
 
## Installation

The only thing you have to do in order to use these scripts, is to fill in the `.variables` file. 

In order to get your **Access Token**, navigate to your *Github settings* and go to the *Developer settings*. Click the *Personal access tokens* tab and hit *Generate new token* in the top right. Copy the token that is generated and paste it in the file. 

Your **Git URL** is simply the URL to your Github profile. For example *https://github.com/WittyAdrian*. 

After filling this in, your `.variables` file should look like this:
```
ACCESS_TOKEN=MY_ACCESS_TOKEN
GIT_URL=MY_GITHUB_URL
```

## F.A.Q.

 - How can I run these scripts from anywhere on my computer?
 
Store them all in a single folder and add that to the PATH variable of your User variables in Windows.

 - How can I make this script run everytime I start my PC, but without seeing it run?
 
Create a new basic Task in your Task Scheduler, point it to the `.bat` file and select "At log on of any user" as the trigger. To hide the output, make sure you check the *Hidden* option and also select "Run whether user is logged on or not". 

 - Task Scheduler is executing the script in the wrong directory, how do I fix it?
 
Go to the properties of your task, open the *Actions* tab and hit the *Edit* button for the action that starts the script. Then in the "Start in (optional):" field, enter the directory in which you want the script to start. Note that inside the `.bat` script is a default `CD` command, so this might also interfere with your execution. If this is the case, simply change the directory parameter given there.
