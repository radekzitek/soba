"""
Schemas for debug and system information endpoints.
"""
from pydantic import BaseModel
from typing import Dict, List, Union

class DatabaseInfo(BaseModel):
    """Database connection and status information"""
    connected: bool
    database_name: str
    host: str
    port: str
    user: str
    sqlalchemy_version: str

class VersionInfo(BaseModel):
    """Version information for system components"""
    backend_version: str
    python_version: str
    fastapi_version: str
    sqlalchemy_version: str
    pydantic_version: str

class DebugInfo(BaseModel):
    """Complete system debug information"""
    versions: VersionInfo
    database: DatabaseInfo
    environment: str  # development/staging/production
    cors_origins: List[str]
    logging_config: Dict[str, Union[str, int]]  # Allow both strings and integers 