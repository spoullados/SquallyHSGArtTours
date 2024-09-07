# SquallyHSGArtTours

Welcome to 9.006 RPV: Unlocking Potential: Realizing Social and Mobile Robots in Action!

Complemented by the course instruction manual, this repository serves as a starting point for your projects. Having:
* installed Virtual Studio (VS) Code with Remote - SSH as an extension
* obtained your OpenAI and Azure Speech Service keys

as outlined in the installation manual, by following the instructions to come you will be able to have a conversation with the Navel Robot.

## Forking the repository

Once all team members (regardless whether their background is technical) have created a GitHub account, one team member needs to "fork" this repository. Doing so will create a copy of this repository that is owned by the same team member. Ensure the forked repository is made "Private" such that other teams cannot view your work. Every team member should then be added as "collaborators" to the project repository.

## Cloning the repository

Since all teams will be working on different projects on the same machine (the robot), certain procedures are to be followed to protect individual projects but also to allow all team members to contribute to their team's work. This section outlines a means of making this possible. It should be noted that there are many possible configurations to achieve the above objectives - what is to come is a method tested and recommended by the course leaders.

Firstly, each team member should configure an SSH key on the robot and associate it with their GitHub account. This is achieved by executing the following commands in the terminal within the ~/.ssh directory:

 `ssh-keygen -f SURNAME_NAME_id`

you will then be prompted to create a passphrase. Since this folder will be shared amongst all course participants, create a passphrase that is strong in order to protect your private key.

You should then add the following text to the "config" file within the same directory:

#SURNAME_NAME <br />
Host github.com-SURNAME_NAME <br />
HostName github.com <br />
IdentityFile ~/.ssh/SURNAME_NAME_id <br />

Note: the command `nano config` should open the relevant file if in the correct directory, allowing for the changes to be made. Pressing Ctrl + O, followed by ENTER and then Ctrl + X should save and exit the file.

Now you need to add the authentication SSH key created to Github. The following instructions can be followed to achieve this:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

With the SSH key generated, added to the config file and to your Github account, one team member can now clone the forked repository from Github to the robot machine. Create a folder/ directory in the robot called "TEAM_X", where X is your team number, and clone the repository using SSH. Instructions can be found here:

https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

## Contribution switch

Given the setup provided, before committing and pushing code to the local and remote repositories respectively, the user name and email are to be adjusted such that the contribution is associated with the correct GitHub account. To ease this process:

Immediately after the repository is cloned, run:

`git remote remove origin`

Each team member should then execute:

`git remote add SURNAME_NAME git@github.com-SURNAME_NAME:USERNAME/REPO.git`

where USERNAME and REPO are the username of the person that forked the original repository and the name of the repository, respectively.

Create a script named "git-switch-config.sh":

`touch git-switch-config.sh`

and occupy it with the following content:

#!/bin/bash <br />
<br />
if [ "$1" == "SURNAME_NAME_1" ]; then <br />
    git config user.name "Personal Name of Team Member 1" <br />
    git config user.email "Team-Member-1-Github-Email@example.com" <br />
elif [ "$1" == "SURNAME_NAME_2" ]; then <br />
    git config user.name "Personal Name of Team Member 2" <br />
    git config user.email "Team-Member-2-Github-Email@example.com" <br />
else <br />
    echo "Usage: $0 {SURNAME_NAME_1|SURNAME_NAME_2}" <br />
    exit 1 <br />
fi <br />

where more elif statements can be added for more team members. 

Make the script executable by running:

`chmod +x switch-git-config.sh`


To commit and push changes to the local and remote repositories respectively, run:

`./switch-git-config.sh SURNAME_NAME`

followed by:

`git push SURNAME_NAME BRANCH_NAME`

In order to further SSH-verify commits with a signature, the following instructions can be followed:

https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key

## Password protecting your work

Since all team will be using the same machine for their projects, you might want to password protect your project folder after pushing changes to your remote repository. A suggestion for how you can do so is by zipping the folder.

`zip -r --encrypt ZIPPED_FOLDER_NAME.zip FOLDER_TO_ZIP_NAME`

This command will prompt you to enter a passphrase. Choose this carefully, and ensure all team members are aware of it. You will need this when unzipping the folder to commence with project work. You would then have to delete your unzipped/ unprotected folder via:

`rm -rf FOLDER_TO_ZIP_NAME`

To unzip the folder, use:

`unzip ZIPPED_FOLDER_NAME.zip`

This methodology allows for tracking of changes despite the deletion of the relevant local directory because the zipped folder containts the .git file which includes all details necessary to pick from where you left off once the folder is unzipped. Ensure you commit and push code prior to zipping. This will allow you to recover your work easily if you forget the password set above, or if you accidentally delete your local directory before zipping.

As there are risks associated with this workflow if not followed as instructed, you are encouraged to look at eCryptfs as an alternative option to encrypt your work.

## Virtual Environment

Once you have cloned your forked repository, you must create a virtual environment within the same directory as the project. That can be achieved by running the following on the command line:

`python -m venv .venv`

The virtual environment is used as a means of isolating Python package installations between different projects. The virutal environment created can be activated within the directory it is contained via:

`source .venv/bin/activate`

and can be deactivated using:

`deactivate`

## Installing packages

To install all the dependencies required for the script provided to work, activate the virtual environment you have created and then run the following command:

`pip install -r requirements.txt`

## Access keys to OpenAI and Azure Cognitive services

By following the instructions in the manual mentioned previously, you can obtain access keys to OpenAI and Azure Speech Services. Input these into the appropriate variables in the .env file, and then run the GettingStartedChat.py script using:

`python GettingStartedChat.py`

Enjoy your chat with Squally and best of luck developing your solution for the course!





