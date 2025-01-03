-- Seed main categories
INSERT INTO main_categories (name, description) VALUES
('Housing', 'Housing and accommodation expenses'),
('Transportation', 'Transportation and vehicle expenses'),
('Food', 'Food and dining expenses'),
('Utilities', 'Utility bills and services'),
('Income', 'All sources of income'),
('Healthcare', 'Medical and healthcare expenses'),
('Entertainment', 'Entertainment and recreation'),
('Shopping', 'Shopping and personal items');

-- Seed sub-categories
INSERT INTO sub_categories (main_category_id, name, description) VALUES
-- Housing
(1, 'Rent', 'Monthly rent payment'),
(1, 'Mortgage', 'Monthly mortgage payment'),
(1, 'Home Insurance', 'Home insurance premium'),
(1, 'Property Tax', 'Property tax payments'),
(1, 'Home Maintenance', 'Home repairs and maintenance'),

-- Transportation
(2, 'Car Payment', 'Monthly car loan payment'),
(2, 'Gas', 'Fuel for vehicles'),
(2, 'Car Insurance', 'Vehicle insurance premium'),
(2, 'Public Transit', 'Public transportation costs'),
(2, 'Car Maintenance', 'Vehicle maintenance and repairs'),

-- Food
(3, 'Groceries', 'Grocery shopping'),
(3, 'Restaurants', 'Dining out'),
(3, 'Take Out', 'Food delivery and takeout'),
(3, 'Coffee Shops', 'Coffee and snacks'),

-- Utilities
(4, 'Electricity', 'Electric utility bills'),
(4, 'Water', 'Water utility bills'),
(4, 'Gas', 'Gas utility bills'),
(4, 'Internet', 'Internet service'),
(4, 'Phone', 'Mobile phone service'),

-- Income
(5, 'Salary', 'Regular employment income'),
(5, 'Bonus', 'Work bonuses'),
(5, 'Investment', 'Investment returns'),
(5, 'Side Gig', 'Additional income sources'),

-- Healthcare
(6, 'Insurance', 'Health insurance premium'),
(6, 'Doctor', 'Doctor visits'),
(6, 'Pharmacy', 'Medications and pharmacy items'),
(6, 'Dental', 'Dental care'),

-- Entertainment
(7, 'Movies', 'Movie tickets and streaming'),
(7, 'Games', 'Video games and gaming'),
(7, 'Hobbies', 'Hobby-related expenses'),
(7, 'Sports', 'Sports and fitness activities'),

-- Shopping
(8, 'Clothing', 'Clothes and accessories'),
(8, 'Electronics', 'Electronic devices'),
(8, 'Home Goods', 'Household items'),
(8, 'Gifts', 'Gifts for others');

-- Seed accounts
INSERT INTO accounts (name, account_type, initial_balance, current_balance, currency, description) VALUES
('Main Checking', 'checking', 5000.00, 5000.00, 'USD', 'Primary checking account'),
('Savings', 'savings', 10000.00, 10000.00, 'USD', 'Emergency fund'),
('Credit Card', 'credit_card', 0.00, 0.00, 'USD', 'Main credit card'),
('Investment Account', 'investment', 25000.00, 25000.00, 'USD', 'Investment portfolio'),
('Cash Wallet', 'cash', 200.00, 200.00, 'USD', 'Physical cash');

-- Seed counterparties
INSERT INTO counterparties (name, is_frequent) VALUES
('Walmart', true),
('Amazon', true),
('Shell Gas', true),
('Netflix', true),
('Local Power Co', true),
('City Water', true),
('Internet Provider', true),
('Employer Inc', true),
('Local Grocery', true),
('Target', true);

-- Create a monthly budget
INSERT INTO budgets (name, start_date, end_date, period, description) VALUES
('Monthly Budget 2024', '2024-01-01', '2024-12-31', 'monthly', 'Monthly budget for 2024');

-- Seed budget items
INSERT INTO budget_items (budget_id, sub_category_id, planned_amount) VALUES
(1, 1, 1500.00),  -- Rent
(1, 11, 500.00),  -- Groceries
(1, 16, 100.00),  -- Electricity
(1, 7, 200.00),   -- Gas
(1, 19, 80.00);   -- Phone

-- Seed some sample transactions
INSERT INTO transactions (
    transaction_date, 
    transaction_type, 
    amount, 
    account_id, 
    counterparty_id, 
    sub_category_id, 
    description
) VALUES
('2024-01-01', 'income', 5000.00, 1, 8, 20, 'Monthly salary'),
('2024-01-02', 'expense', 1500.00, 1, 1, 1, 'Monthly rent'),
('2024-01-03', 'expense', 85.50, 3, 9, 11, 'Weekly groceries'),
('2024-01-03', 'expense', 45.00, 3, 3, 7, 'Gas fill-up'),
('2024-01-04', 'expense', 15.99, 3, 4, 29, 'Monthly subscription'),
('2024-01-05', 'transfer', 1000.00, 1, NULL, NULL, 'Transfer to savings'),
('2024-01-05', 'transfer', 1000.00, 2, NULL, NULL, 'Transfer from checking');

-- Link transfer transactions
INSERT INTO transfer_transactions (from_transaction_id, to_transaction_id)
VALUES (6, 7); 