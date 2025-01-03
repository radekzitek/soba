# Soba - Family Finance Manager

A full-stack application for managing family finances, built with FastAPI and Vue.js.

## Features
- User authentication and registration
- Account management (bank accounts, credit cards, etc.)
- Counterparty management
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
├── schema/           # Database schema
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

4. Initialize database:
```bash
psql -U your_user -d your_database -f finance_db/schema/schema.sql
psql -U your_user -d your_database -f finance_db/seed/seed.sql
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

## Version History
See [CHANGELOG.md](CHANGELOG.md) for version history.

## License
MIT

## Roadmap & Technical Notes

### Recommended Next Steps
1. Transaction Management
   - Implement CRUD operations for transactions
   - Add transaction categories support
   - Create transaction history view
   - Add filtering and search capabilities

2. Reporting & Analytics
   - Monthly spending reports
   - Category-based analysis
   - Budget tracking
   - Income vs. Expense visualization

3. User Experience
   - Mobile-responsive design improvements
   - Bulk operations support
   - Data export functionality
   - Quick actions menu

### Planned Improvements
1. Security Enhancements
   - Two-factor authentication
   - Password reset functionality
   - Session management
   - API rate limiting

2. Performance Optimizations
   - Database query optimization
   - Frontend caching strategy
   - API response compression
   - Lazy loading implementation

3. Feature Additions
   - Multi-currency conversion
   - Recurring transactions
   - File attachments for transactions
   - Budget planning tools

### Technical Debt
1. Database
   - Add proper indexing for performance
   - Implement soft delete pattern
   - Add database migrations tool
   - Optimize foreign key constraints

2. Backend
   - Improve error handling consistency
   - Add comprehensive API tests
   - Implement request validation middleware
   - Enhance logging and monitoring

3. Frontend
   - Add unit tests for components
   - Implement E2E testing
   - Improve state management
   - Add proper TypeScript types

4. DevOps
   - Set up CI/CD pipeline
   - Add automated testing
   - Implement proper backup strategy
   - Add monitoring and alerting
