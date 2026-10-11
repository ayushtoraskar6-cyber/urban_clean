@echo off
title UrbanClean - Live Database Sync Tool
echo ============================================================
echo   Syncing Live Render Cloud Database to Local SQLite...
echo ============================================================
echo.
python "%~dp0sync_live_to_local.py"
echo.
echo Launching DB Browser for SQLite...
start "" "%~dp0DB_Browser_SQLite\DB Browser for SQLite.exe" "%~dp0backend\urban_clean.db"
echo.
echo Done! In DB Browser: Go to 'Browse Data' -> Table: 'accounts' -> Press F5.
timeout /t 5
