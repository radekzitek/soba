import asyncio
import sys
from pathlib import Path
from sqlalchemy import text

# Add the parent directory to Python path to import app modules
sys.path.append(str(Path(__file__).parent.parent.parent))

from app.database import engine

async def test_database_connection():
    try:
        # Try to connect and execute a simple query
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ Successfully connected to the database!")
            
            # Test if we can query the user_table
            result = await conn.execute(text("SELECT * FROM user_table LIMIT 1"))
            print("✅ Successfully queried user_table!")
            
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {str(e)}")
        raise e
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test_database_connection()) 