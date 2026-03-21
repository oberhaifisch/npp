@echo off
REM THIS FILE MUST DO NOTHING
REM echo %%0 %0
REM echo %%1 %1 is CURRENT_DIRECTORY
REM echo %%2 %2 is FULL_CURRENT_PATH
REM echo %%3 %3 is NPP_DIRECTORY
REM echo %%4 %4 is COMMANDS

set CURRENT_DIRECTORY="%1" 
set FULL_CURRENT_PATH="%2" 
set NPP_DIRECTORY="%3" 
set COMMANDS="%4" 

set "PYTHON_PATH=python" 
set "PYTHON_PATH=D:\HyperV\WPy64-3880\python-3.8.8.amd64\python.exe" 
set "PYTHON_PATH=D:\HyperV\WPy64-31330\python\python.exe" 
REM echo PYTHON_PATH %PYTHON_PATH%
REM pause paused

REM python's sys.argv wont work properly if path is drive root   
set COMMANDS_GROUP="CURRENT_DIRECTORY>%1<FULL_CURRENT_PATH>%2<NPP_DIRECTORY>%3<COMMANDS>%4<PYTHON_PATH>%PYTHON_PATH%"
REM echo COMMANDS_GROUP %COMMANDS_GROUP%

if EXIST %2 (
	REM THIS WILL BREAK FOR UNC PATH
	pushd %1
	%PYTHON_PATH% %3\kzr_python_runner.py %COMMANDS_GROUP%
) ELSE (
	REM echo %2 not exists
	pushd %3\backup
	%PYTHON_PATH% ..\kzr_python_runner.py %COMMANDS_GROUP%
)
