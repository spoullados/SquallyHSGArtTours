# SquallyHSGArtTours

Welcome to 9.006 RPV: Unlocking Potential: Realizing Social and Mobile Robots in Action!

This repository serves as a starting point for your projects; by following the instructions to come you will be able to have a conversation with the Navel Robot.

Assuming you have set up you personal computer with all requirements outlined in the "Getting Started" manual (LINK), you need to first "fork" this repository. Every team member should then be included on the project repository, and the repository should be cloned to the robot in a folder named "TEAM_X", where X is your team number (DIRECTORY WHERE THIS SHOULD BE DONE). Please ensure the usernames and emails used to create your Github accounts are the same as the usernames and emails used to configure git settings on the robot when each team member works on the local directory. This will allow git to track individual contributions.

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





