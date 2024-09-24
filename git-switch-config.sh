#!/bin/bash

if [ "$1" == "JONAS_LAENZLINGER" ]; then
   git config user.name "Jonas Länzlinger"
   git config user.email "laenzlinger.jonas@gmail.com"
else
   echo "Usage: $0 {SURNAME_NAME_1|SURNAME_NAME_2}"
   exit 1
fi