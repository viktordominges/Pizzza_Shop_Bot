@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5572026862:AAHM56jRZQ7qscPpkYbUSxzhvVc3kb9mxF8

python bot_telegram.py

pause
