# UrbanClean

A smart urban cleanliness and waste-management web application built for the BSc Computer Science final project at D. G. Ruparel College of Arts, Science & Commerce, Mumbai.

---

## About

UrbanClean allows citizens to report garbage and cleanliness issues with GPS location and photo evidence. Municipal drivers can receive optimised collection routes, and administrators can monitor all complaints and driver activity through a real-time dashboard.

**Project by:** Mr. Ayush Santosh Toraskar (Roll No. CS-9147, Sem-V, 2026–2027)  
**Guide:** Prof. Aarti Gawai  
**College:** Modern Education Society's The D. G. Ruparel College of Arts, Science & Commerce

---

## Features

- **Citizen Portal** — Report complaints with GPS coordinates, category, photo upload, and description. Track complaint status in real time.
- **Driver Portal** — View assigned complaints on an interactive map. Generate an optimised collection route using the Travelling Salesman Problem (Nearest Neighbour greedy algorithm) with OSRM turn-by-turn routing.
- **Admin Dashboard** — View all complaints, manage drivers, see KPI statistics, and export monthly reports as CSV.
- **Multi-role authentication** — PBKDF2/SHA-512 salted password hashing; role-based access control (RBAC) enforced on both frontend and backend.
- **Dual persistence** — All data written to `db.json` is automatically mirrored to a SQLite database via `sync_sqlite.py`.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Node.js · Express 4 · ESM modules |
| File uploads | Multer 1.4 (5 MB limit, images only) |
| Frontend | Vanilla HTML5 · CSS3 · JavaScript (ES6+) |
| Maps | Leaflet.js · OpenStreetMap tiles |
| Route optimisation | OSRM public API · Haversine fallback |
| Primary data store | `db.json` (JSON flat-file) |
| Mirror data store | SQLite (`urban_clean.db`) via `sync_sqlite.py` |
| Build tool | Vite 5 |
| CORS | cors 2.8 |

---

## Project Structure

```
urban_clean/
├── backend/
│   ├── server.js           # Express REST API (ESM)
│   ├── db.json             # Primary data store (seed data)
│   ├── sync_sqlite.py      # SQLite sync script
│   └── ...
├── frontend/
│   ├── index.html          # Landing page
│   ├── login.html          # Multi-role login
│   ├── citizen.html        # Citizen complaint portal
│   ├── driver.html         # Driver route workspace
│   ├── admin.html          # Admin dashboard
│   ├── script.js           # Frontend logic
│   └── styles.css
├── screenshots/
│   └── evidence/           # Testing screenshots (S01–S47)
├── test_suite/
│   ├── unit_tests.js       # Unit tests (Haversine, PBKDF2, TSP)
│   ├── integration_tests.js # API integration tests
│   ├── benchmark_latency.js # Latency benchmark
│   └── verify_db_sync.py   # db.json ↔ SQLite sync audit
├── docs/
│   └── UrbanClean_Complete_Testing_Process_and_Evidence.md
├── .gitignore
└── README.md
```

---

## Running the Application

**Prerequisites:** Node.js 18+, Python 3.x (for sync_sqlite.py)

```bash
# 1. Install backend dependencies
cd backend
npm install

# 2. Start the server
npm start
```

The server starts on **port 3000** by default (configurable via `PORT` environment variable).  
Open your browser at: `http://localhost:3000`

---

## Demo Accounts

These credentials are shown on the login page for demonstration purposes:

| Role | Email | Password |
|---|---|---|
| Citizen | ayush@urbanclean.org | Citizen@123 |
| Driver | ramesh@urbanclean.org | Driver@123 |
| Admin | admin@urbanclean.org | Admin@123 |

---

## REST API Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/api/login` | Authenticate user |
| GET | `/api/complaints` | List all complaints |
| POST | `/api/complaints` | Submit new complaint (multipart/form-data) |
| PATCH | `/api/complaints/:id/status` | Update complaint status |
| GET | `/api/drivers` | List all drivers |
| POST | `/api/route-optimize` | Generate optimised collection route (TSP) |
| GET | `/api/admin/stats` | Dashboard KPI statistics |
| GET | `/api/notifications` | User notifications |

---

## Testing

```bash
# Unit tests
node test_suite/unit_tests.js

# Integration tests (requires server running on port 3000)
node test_suite/integration_tests.js

# Latency benchmark
node test_suite/benchmark_latency.js

# DB sync audit
python test_suite/verify_db_sync.py
```

See [`docs/UrbanClean_Complete_Testing_Process_and_Evidence.md`](docs/UrbanClean_Complete_Testing_Process_and_Evidence.md) for the full testing report.

---

## License

This project is submitted as an academic project for BSc Computer Science, Semester V (2026–2027).
