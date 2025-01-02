Frontend
========
## 1. Vue 3
## 2. Vuetify
## 3. Vue Router
## 4. Pinia
## 5. Axios
## 6. Vite

Directory Structure
-------------------
frontend/
- public/
- src/
    - assets/
    - components/
    - views/
    - App.vue
    - main.js
- package.json


Backend
=======
FastAPI-based backend providing user management and authentication services.

## Features
- RESTful API with FastAPI
- Async PostgreSQL with SQLAlchemy
- JWT Authentication
- Password hashing with bcrypt
- Comprehensive logging
- Health and debug endpoints
- Environment-based configuration

## Directory Structure
```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and endpoints
│   ├── database.py          # Database connection management
│   ├── models/             
│   │   ├── __init__.py
│   │   └── user.py         # SQLAlchemy models
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py         # Pydantic models for user operations
│   │   └── debug.py        # Pydantic models for system info
│   ├── crud/
│   │   ├── __init__.py
│   │   └── user.py         # Database operations
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py       # Application configuration
│   │   ├── security.py     # Authentication utilities
│   │   ├── deps.py         # Dependencies and middleware
│   │   └── logging_config.py # Logging configuration
│   └── tests/
│       ├── __init__.py
│       └── test_db.py      # Database tests
├── logs/                    # Application logs directory
├── requirements.txt         # Python dependencies
└── run.py                  # Application runner
```

## Configuration
The application is configured through environment variables, which can be set in a `.env` file:

```ini
# Version
VERSION=0.1.0                # Application version

# Database settings
DATABASE_USER=user           # PostgreSQL username
DATABASE_PASSWORD=pass       # PostgreSQL password
DATABASE_HOST=localhost      # Database host
DATABASE_PORT=5432          # Database port
DATABASE_NAME=dbname        # Database name

# Security settings
SECRET_KEY=your-secret-key  # JWT signing key
ACCESS_TOKEN_EXPIRE_MINUTES=60  # JWT token expiration time

# Environment settings
ENVIRONMENT=development     # development/staging/production
```

All configuration values are required - the application will fail to start if any are missing.

## Logging
The application uses a comprehensive logging system:
- All logs are written to `logs/app.log`
- Log files are rotated at 1MB size
- Keeps 5 backup files
- Logs include:
  - Database operations
  - Authentication attempts
  - API requests
  - System events
  - Health checks

## API Documentation
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## System Endpoints
- `/health` - Basic health check
- `/debug/system` - Detailed system information including:
  - Version information
  - Database status
  - Environment details
  - Logging configuration
  - CORS settings

## Setup and Running
1. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with required configuration

4. Run the application:
```bash
python run.py
```

The server will start at `http://localhost:8000`

