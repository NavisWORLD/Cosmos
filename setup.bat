@echo off
setlocal
where python >nul 2>&1
if errorlevel 1 (
  echo Python 3.10+ is required.
  exit /b 1
)
if not exist .venv python -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m cosmos doctor
python -m cosmos demo
endlocal
