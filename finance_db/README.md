# Family Finance Manager Database Schema

## Overview
This database schema is designed for a family finance management system. It supports tracking of income, expenses, transfers between accounts, budgeting, and financial planning.

## Database Structure

### Users (`user_table`)
Stores user authentication and profile information.
- `id` - Primary key
- `user_login` - Unique username (VARCHAR(255))
- `user_pass` - Hashed password (VARCHAR(255))
- `user_full_name` - User's full name (VARCHAR(255))
- `user_email` - Unique email address (VARCHAR(255))
- `user_note` - Optional notes (VARCHAR(255))
- `created_at`, `updated_at` - Timestamps

### Accounts (`accounts`)
Financial accounts like bank accounts, credit cards, etc.
- `id` - Primary key
- `name` - Account name (VARCHAR(100))
- `account_type` - ENUM('cash', 'checking', 'savings', 'credit_card', 'investment')
- `initial_balance` - Starting balance (DECIMAL(12,2))
- `current_balance` - Current balance (DECIMAL(12,2))
- `currency` - Three-letter currency code (VARCHAR(3))
- `is_active` - Account status flag (BOOLEAN)
- `description` - Optional description (TEXT)
- `created_at`, `updated_at` - Timestamps

### Main Categories (`main_categories`)
Top-level transaction categories.
- `id` - Primary key
- `name` - Category name (VARCHAR(50))
- `description` - Category description (TEXT)
- `created_at`, `updated_at` - Timestamps

### Sub Categories (`sub_categories`)
Detailed transaction categories within main categories.
- `id` - Primary key
- `main_category_id` - Foreign key to main_categories
- `name` - Sub-category name (VARCHAR(50))
- `description` - Sub-category description (TEXT)
- `created_at`, `updated_at` - Timestamps
- Unique constraint on (main_category_id, name)

### Counterparties (`counterparties`)
Entities involved in transactions (payees/payers).
- `id` - Primary key
- `name` - Counterparty name (VARCHAR(100))
- `description` - Optional description (TEXT)
- `is_active` - Status flag (BOOLEAN)
- `created_at`, `updated_at` - Timestamps

### Transactions (`transactions`)
Financial transactions record.
- `id` - Primary key
- `transaction_date` - Date of transaction (DATE)
- `transaction_type` - ENUM('income', 'expense', 'transfer')
- `amount` - Transaction amount (DECIMAL(12,2))
- `account_id` - Foreign key to accounts
- `counterparty_id` - Foreign key to counterparties
- `sub_category_id` - Foreign key to sub_categories
- `description` - Transaction description (TEXT)
- `notes` - Additional notes (TEXT)
- `is_recurring` - Recurring transaction flag (BOOLEAN)
- `created_at`, `updated_at` - Timestamps

### Transfer Transactions (`transfer_transactions`)
Links pairs of transactions for transfers between accounts.
- `id` - Primary key
- `from_transaction_id` - Foreign key to transactions (source)
- `to_transaction_id` - Foreign key to transactions (destination)
- `created_at` - Timestamp

## Enums
- `account_type`: Types of financial accounts
  - cash
  - checking
  - savings
  - credit_card
  - investment

- `transaction_type`: Types of transactions
  - income
  - expense
  - transfer

- `budget_period`: Budget time periods
  - monthly
  - quarterly
  - yearly

## Timestamps and Triggers
All tables include:
- `created_at` - Record creation timestamp
- `updated_at` - Last modification timestamp
- Automatic trigger to update `updated_at` on record modification

## Constraints
- Main category names are unique
- Sub-category names are unique within their main category
- Counterparty names are unique
- All foreign keys are properly constrained
- Decimal fields use (12,2) precision for monetary values

## Usage
1. Create database and user:
```sql
CREATE DATABASE soba_finance;
CREATE USER soba_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE soba_finance TO soba_user;
```

2. Initialize schema:
```bash
psql -U soba_user -d soba_finance -f schema.sql
```

3. Load sample data (optional):
```bash
psql -U soba_user -d soba_finance -f seed.sql
```

## Notes
- All monetary values use DECIMAL(12,2) for precision
- Timestamps use timezone-aware type
- Soft deletion implemented via is_active flags
- Transfer transactions are linked pairs for account-to-account transfers 