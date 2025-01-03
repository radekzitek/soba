-- Add updated_at column to user_table
ALTER TABLE user_table 
ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP;

-- Add trigger to automatically update updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_user_table_updated_at 
    BEFORE UPDATE ON user_table 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column(); 