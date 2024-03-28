@echo off

REM Check if a virtual environment already exists
if exist venv (
    echo Virtual environment already exists. Activating and updating dependencies...
    venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
) else (
    REM Create a virtual environment
    python -m venv venv
    echo Virtual environment created. Activating and updating dependencies...
    venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
)