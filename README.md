# SquallyHSGArtTours

Welcome to 9.006 RPV: Unlocking Potential: Realizing Social and Mobile Robots in Action!

Complemented by the course instruction manual, this repository serves as a starting point for your projects. Having installed Virtual Studio (VS) Code and Remote - SSH as an extension, as outlined in the installation manual, by following the instructions to come you will be able to have a conversation with the Navel Robot.

## Forking the repository

Once all team members (regardless whether their background is technical) have created a GitHub account, one team member needs to "fork" this repository. Doing so will create a copy of this repository that is owned by the same team member. Ensure the forked repository is made "Private" such that other teams cannot view your work. Every team member should then be added as "collaborators" to the project repository.

## Cloning the repository

Since all teams will be working on different projects on the same machine (the robot), certain procedures are to be followed to protect individual projects but also to allow all team members to contribute to their team's work. This section outlines a means of making this possible.

Firstly, each team member should configure an SSH key on the robot and associate it with their GitHub account. This is achieved by executing the following commands in the terminal within the ~/.ssh directory:

 `ssh-keygen -f SURNAME_NAME_id`

you will then be prompted to create a passphrase. Since this folder will be shared amongst all course participants, create a passphrase that is strong in order to protect your private key.

You should then add the following text to the "config" file within the same directory:

#SURNAME_NAME
Host github.com-SURNAME_NAME 
HostName github.com
IdentityFile ~/.ssh/SURNAME_NAME_id


and the repository should be cloned to the robot in a folder named "TEAM_X", where X is your team number (DIRECTORY WHERE THIS SHOULD BE DONE). 

NOTEEEE: Please ensure the usernames and emails used to create your Github accounts are the same as the usernames and emails used to configure git settings on the robot when each team member works on the local directory. This will allow git to track individual contributions.

## Virtual Environment

Once you have cloned your forked team repository, you must create a virtual environment within the same directory as the project. That can be achieved by running the following on the command line:

`python -m venv .venv`

The virtual environment is used as a means of isolating Python package installations between different projects. The virutal environment created can be activated within the directory it is contained via:

`source .venv/bin/activate`

and can be deactivated using:

`deactivate`

## Installing packages

To install all the dependencies required for the script provided to work, activate the virtual environment you have created and then run the following command:

`pip install -r requirements.txt`

## Access keys to OpenAI and Azure Cognitive services

By following the instructions in the manual mentioned previously, you can obtain access keys to OpenAI and Azure Cognitive Services. Input these into the appropriate variables in the GettingStartedChat.py script, and then you can run the same code using:

`python GettingStartedChat.py`

Enjoy your chat with Squally and best of luck developing your solution for the course!





