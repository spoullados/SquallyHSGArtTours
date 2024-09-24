#!/bin/bash

if [ "$1" == "JONAS_LAENZLINGER" ]; then
   git config user.name "jonaslanzlinger"
   git config user.email "laenzlinger.jonas@gmail.com"
elif [ "$1" == "SURNAME_NAME_2" ]; then
   git config user.name "Personal Name of Team Member 2"
   git config user.email "Team-Member-2-Github-Email@example.com"
else
   echo "Usage: $0 {SURNAME_NAME_1|SURNAME_NAME_2}"
   exit 1
fi