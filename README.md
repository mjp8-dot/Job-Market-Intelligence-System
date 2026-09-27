# Job Market Intelligence System

A Python-based job market intelligence system that collects job listings from the **Adzuna API**, stores them in **PostgreSQL**, and provides a CLI-based interface for searching and viewing job data.

The project focuses on applying **Python, HTTP/API communication, PostgreSQL, SQL, OOP, error handling, and modular software architecture** in a practical system.

## Features

- Fetch job listings from the Adzuna API
- Store job data in PostgreSQL
- Prevent duplicate jobs using unique job IDs
- Automatically initialize the database table
- Search jobs using:
  - Keyword
  - Location
  - Category
- PostgreSQL full-text search using `to_tsvector()` and `plainto_tsquery()`
- Case-insensitive filtering using `ILIKE`
- View all stored jobs
- CLI-based dashboard
- HTTP and database error handling
- Modular architecture separating API, database, dashboard, and orchestration logic
- PostgreSQL GIN index for faster text searching

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Requests | HTTP/API communication |
| Adzuna API | Job listing data source |
| PostgreSQL | Persistent data storage |
| psycopg2 | PostgreSQL connectivity |
| SQL | Data storage and querying |
| Git/GitHub | Version control |

## Architecture

The application follows a modular architecture where the **Manager acts as the central orchestrator**.

```text
                    ┌─────────────┐
                    │   main.py   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Manager   │
                    └──────┬──────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        ┌─────────┐   ┌─────────┐   ┌────────────┐
        │   API   │   │  PSQL   │   │ Dashboard  │
        └─────────┘   └─────────┘   └────────────┘
             │             │              │
             ▼             ▼              ▼
         Adzuna API    PostgreSQL      CLI Input
