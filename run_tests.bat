REM Activating Virtual Enviroment
python -m venv venv
CALL venv\Scripts\activate.bat

REM Installing Python Dependencies
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pytest src/tests

rmdir /s /q venv
