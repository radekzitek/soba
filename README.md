# System Debug Dashboard

A full-stack application for system monitoring and debugging, built with FastAPI and Vue.js.

## Features
- Real-time system information monitoring
- Database connection status
- Environment configuration display
- Logging system overview
- Version tracking
- Health checks

## Technology Stack
### Backend
- FastAPI for REST API
- Async PostgreSQL with SQLAlchemy
- JWT Authentication
- Comprehensive logging system
- Environment-based configuration

### Frontend
- Vue 3 with Composition API
- TypeScript for type safety
- Vuetify 3 for UI components
- Pinia for state management
- Axios for API communication
- Vite for development and building

## Directory Structure
```
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py       # Application configuration
│   │   │   ├── security.py     # Authentication utilities
│   │   │   └── logging_config.py # Logging setup
│   │   ├── models/            
│   │   ├── schemas/
│   │   └── crud/
│   ├── logs/                   # Application logs
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── system/        # System info components
│   │   │   └── SystemDebug.vue
│   │   ├── stores/
│   │   │   └── system.ts      # Pinia store
│   │   ├── types/
│   │   │   └── system.ts      # TypeScript interfaces
│   │   └── config/
│   │       └── index.ts       # Frontend configuration
│   └── package.json
```

## Configuration

### Backend (.env)
```ini
# Version
VERSION=0.1.0

# Database settings
DATABASE_USER=user
DATABASE_PASSWORD=pass
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=dbname

# Security settings
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Environment settings
ENVIRONMENT=development
```

### Frontend (.env)
```ini
VITE_API_BASE_URL=/api
```

## Setup and Running

### Backend
1. Create Python virtual environment:
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

### Frontend
1. Install dependencies:
```bash
cd frontend
npm install
```

2. Run development server:
```bash
npm run dev
```

3. Build for production:
```bash
npm run build
```

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## System Endpoints
- `/health` - Basic health check
- `/debug/system` - Detailed system information

## Development

### Backend
- Uses FastAPI's async features
- Comprehensive logging with rotation
- Environment-based configuration
- Type checking with Pydantic

### Frontend
- TypeScript for type safety
- Component-based architecture
- Centralized state management
- Proxy configuration for API calls
- Environment configuration

## Logging
All backend logs are written to `logs/app.log` with:
- Automatic rotation at 1MB
- Keeps 5 backup files
- Comprehensive logging of:
  - Database operations
  - API requests
  - System events
  - Health checks

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Version History
See [CHANGELOG.md](CHANGELOG.md) for version history.

