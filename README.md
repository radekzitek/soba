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
- FastAPI with async/await support
- SQLAlchemy 2.0 with async drivers
- PostgreSQL with asyncpg
- JWT Authentication
- Pydantic 2.0 for data validation
- Comprehensive logging system
- Class-based CRUD operations
- Environment-based configuration
- Automated database migrations

### Frontend
- Vue 3 with Composition API
- Vuetify 3 for UI components
- Pinia for state management
- Axios for API communication
- TypeScript support
- Component-based architecture

## Project Structure
```
backend/
├── app/
│   ├── core/          # Core functionality (auth, config, logging)
│   ├── crud/          # Database operations
│   ├── models/        # SQLAlchemy models
│   ├── routers/       # API endpoints
│   └── schemas/       # Pydantic schemas
frontend/
├── src/
│   ├── components/    # Vue components
│   ├── views/         # Page components
│   ├── stores/        # Pinia stores
│   └── services/      # API services
finance_db/
├── schema/           # Database schema and migrations
└── seed/            # Sample data for development
```

## Getting Started
### Backend Setup
1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables in `.env`

4. Run migrations:
```bash
psql -U your_user -d your_database -f finance_db/schema/01_create_tables.sql
psql -U your_user -d your_database -f finance_db/schema/02_add_timestamps.sql
```

5. Start the server:
```bash
python run.py
```

### Frontend Setup
1. Install dependencies:
```bash
npm install
```

2. Start development server:
```bash
npm run dev
```

## API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
MIT
