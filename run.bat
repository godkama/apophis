@echo off

REM Upgrade pip
py -m pip install --upgrade pip

REM Install requirements from requirements.txt
py -m pip install -r requirements.txt

cls

REM Run main.py
py main.py
