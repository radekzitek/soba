# Soba - System Debug Dashboard

A full-stack application for system monitoring and debugging, built with FastAPI and Vue.js.

## Features
- Real-time system monitoring
- User authentication and registration
- Dark/Light theme support
- Frontend and backend version tracking
- Database connection monitoring
- Environment configuration display
- Logging system overview
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
│   │   │   ├── deps.py         # Dependencies and middleware
│   │   │   └── logging_config.py # Logging setup
│   │   ├── models/            
│   │   ├── schemas/
│   │   └── crud/
│   ├── logs/                   # Application logs
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/         # Vue components
│   │   ├── views/             # Page components
│   │   ├── stores/            # Pinia stores
│   │   └── config/            # Frontend configuration
│   └── package.json
```

## Configuration

### Backend (.env)
```ini
VERSION=0.1.2
DATABASE_USER=user
DATABASE_PASSWORD=pass
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=dbname
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=60
ENVIRONMENT=development
```

### Frontend (.env)
```ini
VITE_APP_VERSION=0.1.2
VITE_APP_NAME=Soba
VITE_API_BASE_URL=/api
VITE_APP_ENV=development
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

## Key Endpoints
- `/health` - Basic health check
- `/debug/system` - Detailed system information
- `/token` - User authentication
- `/users/me` - Current user information
- `/users/` - User management

## Features
### Authentication
- JWT-based authentication
- User registration and login
- Secure password hashing
- Protected routes

### System Monitoring
- Frontend versions display
- Backend versions tracking
- Database connection status
- Environment configuration
- Logging system overview

### User Interface
- Responsive grid layout
- Dark/Light theme switching
- Real-time data updates
- User-friendly forms
- Error handling

## Logging
All backend logs are written to `logs/app.log` with:
- Automatic rotation at 1MB
- Keeps 5 backup files
- Comprehensive logging of:
  - API requests and responses
  - Database operations
  - System events
  - Authentication attempts

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Version History
See [CHANGELOG.md](CHANGELOG.md) for version history.

