# Soba - Family Finance Manager

A full-stack application for managing family finances, built with FastAPI and Vue.js.

## Features
- User authentication and registration
- Account management (bank accounts, credit cards, etc.)
- Dark/Light theme support
- System monitoring and debugging
- Multi-currency support
- Real-time data updates

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

## Project Structure
```
├── backend/
│   ├── app/
│   │   ├── core/          # Core functionality
│   │   ├── routers/       # API routes
│   │   ├── models/        # Database models
│   │   ├── schemas/       # Pydantic schemas
│   │   └── crud/          # Database operations
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/    # Vue components
│   │   ├── views/         # Page components
│   │   ├── stores/        # Pinia stores
│   │   └── services/      # API services
│   └── package.json
│
└── finance_db/            # Database schema and seeds
    ├── schema/
    └── seed/
```

## Features
### Account Management
- Create and manage multiple accounts
- Track account balances
- Support for different account types
- Multi-currency support
- Active/Inactive status tracking

### User Management
- User registration and authentication
- JWT-based security
- User profile management

### System Features
- Dark/Light theme
- Real-time data updates
- System monitoring
- Comprehensive logging

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

## Database Schema
See [finance_db/README.md](finance_db/README.md) for detailed database documentation.

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Version History
See [CHANGELOG.md](CHANGELOG.md) for version history.
