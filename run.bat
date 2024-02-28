REM Activating Virtual Enviroment
python -m venv venv
CALL venv\Scripts\activate.bat

REM Installing Python Dependencies
python -m pip install -r requirements.txt
python tasklist.py

rmdir /s /q venv