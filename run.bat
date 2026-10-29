@echo off
setlocal enabledelayedexpansion
title MediAlert Pro Web Application Launcher
color 0b

echo ====================================================================
echo        MediAlert Pro - Clinical Pharmacy Inventory Web System
echo ====================================================================
echo.

cd /d "%~dp0"

:: Detect Python executable
set "PYTHON_EXE="
where python >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_EXE=python"
) else (
    where py >nul 2>&1
    if %errorlevel% equ 0 (
        set "PYTHON_EXE=py -3"
    )
)

if "%PYTHON_EXE%"=="" (
    color 0c
    echo [ERROR] Python was not found in your system PATH!
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [*] Detected Python command: %PYTHON_EXE%
%PYTHON_EXE% --version
echo.

:: Check required libraries
echo [*] Checking dependencies (Flask, Flask-Login, APScheduler)...
%PYTHON_EXE% -c "import flask, flask_login, apscheduler" >nul 2>&1
if %errorlevel% neq 0 (
    color 0e
    echo [*] Missing dependencies detected. Installing required packages...
    %PYTHON_EXE% -m pip install flask flask-login apscheduler
    if %errorlevel% neq 0 (
        color 0c
        echo [ERROR] Failed to install packages. Please check your internet connection.
        pause
        exit /b 1
    )
    echo [*] Packages successfully installed!
    color 0b
)

echo [*] Launching MediAlert Pro Web Application...
echo [*] Opening browser at http://127.0.0.1:5000 ...
echo.

%PYTHON_EXE% run_web.py

if %errorlevel% neq 0 (
    color 0c
    echo.
    echo [ERROR] The server stopped unexpectedly.
    echo See error details above.
)

echo.
pause
