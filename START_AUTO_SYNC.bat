@echo off
title UrbanClean - Live Automatic Background Sync
color 0A
cls
echo ==============================================================
echo   UrbanClean Live Cloud Automatic Database Sync
echo   Target: https://urban-clean-mp3b.onrender.com
echo ==============================================================
echo.
echo  This window will automatically poll Render every 10 seconds.
echo  Whenever anyone registers or creates a complaint on the live
echo  website, your local SQLite (urban_clean.db) updates automatically!
echo.
echo  Leave this window minimized during your presentation.
echo  Press Ctrl+C to stop at any time.
echo --------------------------------------------------------------
echo.
python "%~dp0sync_live_to_local.py" --watch
pause
