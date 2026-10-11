"""
UrbanClean - Live Render to Local SQLite Sync Script
Synchronizes cloud database (complaints, accounts, drivers, routes) from the
live Render deployment directly into your local SQLite database (backend/urban_clean.db).
"""

import urllib.request
import json
import os
import subprocess
import sys

LIVE_URL = "https://urban-clean-mp3b.onrender.com"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
DB_JSON_PATH = os.path.join(BACKEND_DIR, "db.json")
SQLITE_SYNC_SCRIPT = os.path.join(BACKEND_DIR, "sync_sqlite.py")
SQLITE_DB_PATH = os.path.join(BACKEND_DIR, "urban_clean.db")

def main():
    print("=" * 60)
    print("  UrbanClean: Live Cloud -> Local SQLite Sync Tool")
    print(f"  Target: {LIVE_URL}")
    print("=" * 60)

    try:
        # 1. Try to fetch full DB dump from live Render
        dump_url = f"{LIVE_URL}/api/database/dump"
        req = urllib.request.Request(dump_url, headers={'User-Agent': 'UrbanClean-Sync/1.0'})
        
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                live_data = json.loads(response.read().decode('utf-8'))
                print(">>> Successfully downloaded full database from Render!")
        except Exception:
            # Fallback: fetch complaints and merge with local accounts if dump not yet deployed
            print(">>> Downloading complaints from live deployment...")
            comp_url = f"{LIVE_URL}/api/complaints"
            with urllib.request.urlopen(comp_url, timeout=30) as comp_res:
                live_complaints = json.loads(comp_res.read().decode('utf-8'))
            
            with open(DB_JSON_PATH, 'r', encoding='utf-8') as f:
                live_data = json.load(f)
            live_data['complaints'] = live_complaints

        # 2. Save into local backend/db.json
        with open(DB_JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(live_data, f, indent=2)
        print(f">>> Updated local {DB_JSON_PATH}")

        # 3. Run sync_sqlite.py to rebuild local urban_clean.db
        subprocess.run([sys.executable, SQLITE_SYNC_SCRIPT], check=True)
        print(f">>> Updated local SQLite: {SQLITE_DB_PATH}")

        # 4. Print Summary
        accounts = live_data.get('accounts', {})
        total_accounts = sum(len(v) for v in accounts.values()) if isinstance(accounts, dict) else 0
        total_complaints = len(live_data.get('complaints', []))
        
        print("\n" + "-" * 60)
        print(f"  SYNC COMPLETE!")
        print(f"  Total Accounts in SQLite:   {total_accounts}")
        print(f"  Total Complaints in SQLite: {total_complaints}")
        print("-" * 60)
        print("\nNow you can open DB Browser for SQLite and see all live data:")
        print(f'  & "{BASE_DIR}\\DB_Browser_SQLite\\DB Browser for SQLite.exe" "{SQLITE_DB_PATH}"\n')

    except Exception as e:
        print(f"[Error] Failed to sync live database: {e}")

if __name__ == "__main__":
    main()
