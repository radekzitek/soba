# Family Finance Manager Database Schema

## Overview
This database schema is designed for a family finance management system. It supports tracking of income, expenses, transfers between accounts, budgeting, and financial planning.

## Tables

### Main Categories (`main_categories`)
Top-level categorization for transactions and budgets.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(50) | Unique category name |
| description | TEXT | Category description |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Sub Categories (`sub_categories`)
Detailed categorization linked to main categories.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| main_category_id | INTEGER | Reference to main category |
| name | VARCHAR(50) | Sub-category name |
| description | TEXT | Sub-category description |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Accounts (`accounts`)
Financial accounts for tracking balances and transactions.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(100) | Account name |
| account_type | account_type | Type of account (enum) |
| initial_balance | DECIMAL(12,2) | Starting balance |
| current_balance | DECIMAL(12,2) | Current balance |
| currency | VARCHAR(3) | Currency code (default 'USD') |
| is_active | BOOLEAN | Account status |
| description | TEXT | Account description |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Counterparties (`counterparties`)
Entities involved in transactions (payees/payers).
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(100) | Unique counterparty name |
| description | TEXT | Description |
| website | VARCHAR(255) | Website URL |
| is_frequent | BOOLEAN | Frequently used flag |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Transactions (`transactions`)
Financial transactions record.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| transaction_date | DATE | Date of transaction |
| transaction_type | transaction_type | Type (income/expense/transfer) |
| amount | DECIMAL(12,2) | Transaction amount |
| account_id | INTEGER | Reference to account |
| counterparty_id | INTEGER | Reference to counterparty |
| sub_category_id | INTEGER | Reference to sub-category |
| description | TEXT | Transaction description |
| notes | TEXT | Additional notes |
| is_recurring | BOOLEAN | Recurring transaction flag |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Transfer Transactions (`transfer_transactions`)
Links pairs of transactions for account transfers.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| from_transaction_id | INTEGER | Source transaction reference |
| to_transaction_id | INTEGER | Destination transaction reference |
| created_at | TIMESTAMP | Record creation timestamp |

### Budgets (`budgets`)
Budget period definitions.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| name | VARCHAR(100) | Budget name |
| start_date | DATE | Budget start date |
| end_date | DATE | Budget end date |
| period | budget_period | Period type (monthly/quarterly/yearly) |
| description | TEXT | Budget description |
| is_active | BOOLEAN | Active budget flag |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Budget Items (`budget_items`)
Individual budget allocations per category.
| Column | Type | Description |
|--------|------|-------------|
| id | SERIAL | Primary key |
| budget_id | INTEGER | Reference to budget |
| sub_category_id | INTEGER | Reference to sub-category |
| planned_amount | DECIMAL(12,2) | Budgeted amount |
| notes | TEXT | Additional notes |
| created_at | TIMESTAMP | Record creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

## Custom Types

### transaction_type
- `income`: Money received
- `expense`: Money spent
- `transfer`: Money moved between accounts

### account_type
- `cash`: Physical cash
- `checking`: Checking account
- `savings`: Savings account
- `credit_card`: Credit card account
- `investment`: Investment account

### budget_period
- `monthly`: Monthly budget
- `quarterly`: Quarterly budget
- `yearly`: Yearly budget

## Indexes
- `idx_transactions_date`: Transaction date lookup
- `idx_transactions_type`: Transaction type filtering
- `idx_transactions_account`: Account transactions lookup
- `idx_transactions_category`: Category transactions lookup
- `idx_budget_items_budget`: Budget items lookup
- `idx_budget_dates`: Budget period lookup

## Triggers
All tables have an `updated_at` trigger that automatically updates the timestamp when records are modified.

## Constraints
- Main category names are unique
- Sub-category names are unique within their main category
- Counterparty names are unique
- Budget items are unique per budget and sub-category combination
- All foreign keys are properly constrained
- Decimal fields use (12,2) precision for monetary values 