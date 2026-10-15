@echo off
title UrbanClean - Live Sync and Open SQLite Database
echo ============================================================
echo   Syncing Latest Cloud Data from Render into SQLite...
echo ============================================================
python "%~dp0sync_live_to_local.py"
echo.
echo Launching DB Browser with Updated UrbanClean SQLite Database...
start "" "%~dp0DB_Browser_SQLite\DB Browser for SQLite.exe" "%~dp0backend\urban_clean.db"
exit
