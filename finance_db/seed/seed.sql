-- Seed main categories
INSERT INTO main_categories (name, description) VALUES
('Housing', 'Housing and accommodation expenses'),
('Transportation', 'Transportation and vehicle expenses'),
('Food', 'Food and dining expenses'),
('Utilities', 'Utility bills and services'),
('Income', 'All sources of income'),
('Healthcare', 'Medical and healthcare expenses'),
('Entertainment', 'Entertainment and recreation'),
('Shopping', 'General shopping and purchases');

-- Seed sub-categories
INSERT INTO sub_categories (main_category_id, name, description) VALUES
-- Housing
(1, 'Rent', 'Monthly rent payment'),
(1, 'Mortgage', 'Monthly mortgage payment'),
(1, 'Insurance', 'Home insurance'),
-- Transportation
(2, 'Fuel', 'Vehicle fuel'),
(2, 'Public Transport', 'Bus, train, etc.'),
(2, 'Car Maintenance', 'Vehicle repairs and maintenance'),
-- Food
(3, 'Groceries', 'Food and household items'),
(3, 'Restaurants', 'Eating out'),
(3, 'Takeaway', 'Food delivery and takeout'),
-- Utilities
(4, 'Electricity', 'Electric utility bills'),
(4, 'Water', 'Water utility bills'),
(4, 'Internet', 'Internet service'),
-- Income
(5, 'Salary', 'Regular employment income'),
(5, 'Bonus', 'Work bonuses'),
(5, 'Investment', 'Investment returns'),
-- Healthcare
(6, 'Doctor', 'Doctor visits'),
(6, 'Pharmacy', 'Medications and pharmacy items'),
(6, 'Insurance', 'Health insurance'),
-- Entertainment
(7, 'Movies', 'Cinema and streaming'),
(7, 'Games', 'Video games and entertainment'),
(7, 'Sports', 'Sports activities and equipment'),
-- Shopping
(8, 'Clothing', 'Clothes and accessories'),
(8, 'Electronics', 'Electronic devices'),
(8, 'Home', 'Home goods and furniture');

-- Seed counterparties
INSERT INTO counterparties (name, description, is_active) VALUES
('Local Grocery Store', 'Main grocery store', true),
('City Power Co', 'Electricity provider', true),
('Internet Provider', 'Internet service provider', true),
('Local Gas Station', 'Regular fuel station', true),
('Employer Inc', 'Main employer', true),
('Cinema World', 'Local cinema', true),
('Health Insurance Co', 'Health insurance provider', true),
('Local Restaurant', 'Favorite restaurant', true),
('Public Transport Co', 'City transport provider', true),
('Online Store', 'E-commerce platform', true);

-- Seed accounts
INSERT INTO accounts (name, account_type, initial_balance, current_balance, currency, description) VALUES
('Main Checking', 'checking', 5000.00, 5000.00, 'USD', 'Primary checking account'),
('Savings', 'savings', 10000.00, 10000.00, 'USD', 'Emergency fund'),
('Credit Card', 'credit_card', 0.00, 0.00, 'USD', 'Main credit card'),
('Cash Wallet', 'cash', 200.00, 200.00, 'USD', 'Physical cash'),
('Investment Account', 'investment', 20000.00, 20000.00, 'USD', 'Stock investment account');

-- Seed test user (password is 'test1234')
INSERT INTO user_table (
    user_login,
    user_pass,
    user_full_name,
    user_email
) VALUES (
    'testuser',
    '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewLxrCHGGH0Hx/Y.',
    'Test User',
    'test@example.com'
);

-- Seed transactions
INSERT INTO transactions (
    transaction_date,
    transaction_type,
    amount,
    account_id,
    counterparty_id,
    sub_category_id,
    description,
    is_recurring
) VALUES
-- Income
('2024-01-01', 'income', 5000.00, 1, 5, 13, 'Monthly salary', true),
('2024-01-15', 'income', 1000.00, 1, 5, 14, 'Performance bonus', false),
-- Expenses
('2024-01-02', 'expense', 1500.00, 1, 1, 1, 'Monthly rent', true),
('2024-01-03', 'expense', 100.00, 3, 2, 10, 'Electricity bill', true),
('2024-01-04', 'expense', 80.00, 3, 3, 12, 'Internet bill', true),
('2024-01-05', 'expense', 50.00, 3, 4, 4, 'Gas fill-up', false),
('2024-01-06', 'expense', 120.00, 3, 1, 7, 'Weekly groceries', false),
('2024-01-07', 'expense', 45.00, 3, 8, 8, 'Dinner out', false),
('2024-01-08', 'expense', 200.00, 1, 7, 18, 'Health insurance', true),
('2024-01-09', 'expense', 30.00, 4, 6, 20, 'Movie night', false);

-- Seed transfer transactions
INSERT INTO transactions (
    transaction_date,
    transaction_type,
    amount,
    account_id,
    description,
    is_recurring
) VALUES
('2024-01-10', 'transfer', 1000.00, 1, 'Transfer to savings', false),
('2024-01-10', 'transfer', 1000.00, 2, 'Transfer from checking', false);

-- Link transfer transactions
INSERT INTO transfer_transactions (from_transaction_id, to_transaction_id)
VALUES (
    (SELECT id FROM transactions WHERE description = 'Transfer to savings'),
    (SELECT id FROM transactions WHERE description = 'Transfer from checking')
); 