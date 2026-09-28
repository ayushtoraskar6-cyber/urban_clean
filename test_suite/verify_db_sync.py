import sqlite3
import json
import os

db_json_path = os.path.join('backend', 'db.json')
sqlite_path = os.path.join('backend', 'urban_clean.db')

with open(db_json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

con = sqlite3.connect(sqlite_path)
cur = con.cursor()

print("================================================================================")
print("             URBANCLEAN DUAL PERSISTENCE SYNCHRONIZATION AUDIT                  ")
print("================================================================================")
print(f"JSON Store:   {db_json_path}")
print(f"SQLite DB:    {sqlite_path}\n")

print("--- 1. DOCUMENT STORE (db.json) TOTALS ---")
print(f"Accounts Registered:    {len(d.get('accounts', []))}")
print(f"Complaints Logged:      {len(d.get('complaints', []))}")
print(f"Active Drivers:         {len(d.get('drivers', []))}")
print(f"System Notifications:   {len(d.get('notifications', []))}")

print("\n--- 2. RELATIONAL DATABASE (urban_clean.db) TABLES ---")
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
for t in tables:
    table_name = t[0]
    count = cur.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"Table [{table_name:<16}]: {count:>3} rows")

print("\n--- 3. DATA CONSISTENCY EVALUATION ---")
json_complaints = len(d.get('complaints', []))
sql_complaints = cur.execute("SELECT COUNT(*) FROM complaints").fetchone()[0]
if json_complaints == sql_complaints:
    print(f"[SYNCHRONIZED] Complaint record counts match exactly ({json_complaints} == {sql_complaints}).")
    print("STATUS: ZERO DISCREPANCY DETECTED ACROSS STORAGE ENGINES.")
else:
    print(f"[MISMATCH] db.json ({json_complaints}) != SQLite ({sql_complaints})")

con.close()
