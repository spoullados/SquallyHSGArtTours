# SquallyHSGArtTours

Welcome to 9.006 RPV: Unlocking Potential: Realizing Social and Mobile Robots in Action!

Complemented by the course instruction manual, this repository serves as a starting point for your projects. Having:
* installed Virtual Studio (VS) Code with Remote - SSH as an extension
* obtained your OpenAI and Azure Speech Service keys

as outlined in the installation manual, by following the instructions to come you will be able to have a conversation with the Navel Robot.

## Forking the repository

Once all team members (regardless whether their background is technical) have created a GitHub account, one team member needs to "fork" this repository. Doing so will create a copy of this repository that is owned by the same team member. Ensure the forked repository is made "Private" such that other teams cannot view your work. Every team member, in addition to the course leaders, should then be added as "collaborators" to the project repository.

Since the repository will serve as a project portfolio, and can be edited via Github directly to reflect progress and milestones reached, all members of the team can contribute to it.

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

Now you need to add the authentication SSH key created to Github. To do so you first need to obtain your public key. This is possible by copying the output of the following command:

`cat ~/.ssh/SURNAME_NAME_id.pub`

You can then following the instructions in:

https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

from point 2 onwards, in the "Adding a new SSH key to your account" section. Ensure the key is of type "Authentication".

With the SSH key generated, added to the config file and to your Github account, one team member can now clone the forked repository from Github to the robot machine. Create a folder/ directory in the "Student_Projects" directory called "TEAM_X", where X is your team number:

`cd ~/Student_Projects`

`mkdir Team_X`

and then clone your repository in the directory created using the SSH method referred to in the "Cloning a repository" section provided in the following link:

https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

Note, the person cloning the repository should ammend the command in point 6 in the following manner:

`git clone https://github.com-SURNAME_NAME/YOUR-USERNAME/YOUR-REPOSITORY`

i.e. by appending their SURNAME_NAME to github.com - as specified in the config file edited earlier. You should then provide your SSH key password.

## Virtual Environment

Since various teams will be working on different python scripts which may have conflicting dependencies i.e. different versions of the same packages, it is important for each team to create a virtual environment consisting of an isolated set of installed packages.

Once you have cloned your forked repository, you can create a virtual environment within the same directory as the project via:

`python -m venv .venv`

The virutal environment created can be activated within the directory it is contained via:

`source .venv/bin/activate`

and can be deactivated using:

`deactivate`

## Installing packages

To install all the dependencies required for the script provided to work, activate the virtual environment you have created and then run the following command:

`pip install -r requirements.txt`

## Access keys to OpenAI and Azure Cognitive services

By following the instructions in the manual mentioned previously, you can obtain access keys to OpenAI and Azure Speech Services. 

You should then create a .env file in your project directory via:

`touch .env`

and input the following within the folder:

OPENAI_KEY = "ENTER YOUR OPENAI KEY HERE" <br /> 
AZURE_KEY = "ENTER YOUR AZURE KEY HERE"

where you need to replace the text with the access codes you created. You will then be able to run the GettingStartedChat.py script using:

`python GettingStartedChat.py`

Note: you may need to use "python3" instead of "python"

Enjoy your chat with Squally and best of luck developing your solution for the course!





