#!/bin/bash

clear
source venv/bin/activate
python3 main.py $1 $2
deactivate