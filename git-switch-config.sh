#!/bin/bash

if [ "$1" == "JONAS_LAENZLINGER" ]; then
   git config user.name "Jonas Länzlinger"
   git config user.email "laenzlinger.jonas@gmail.com"
elif [ "$1" == "SASKIA_BILANG" ]; then
   git config user.name "Saskia Bilang"
   git config user.email "saskia.bilang@hispeed.ch"
elif [ "$1" == "PIA_OBENAUF" ]; then
   git config user.name "Pia Obenauf"
   git config user.email "pia.obenauf@student.unisg.ch"

else
   echo "Usage: $0 {SURNAME_NAME_1|SURNAME_NAME_2}"
   exit 1
fi