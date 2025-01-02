/**
 * System information types for the debug interface
 */

export interface VersionInfo {
  backend_version: string
  python_version: string
  fastapi_version: string
  sqlalchemy_version: string
  pydantic_version: string
}

export interface DatabaseInfo {
  connected: boolean
  database_name: string
  host: string
  port: string
  user: string
  sqlalchemy_version: string
}

export interface LoggingConfig {
  log_level: string
  log_file: string
  log_format: string
  max_file_size: string
  backup_count: number
}

export interface SystemInfo {
  versions: VersionInfo
  database: DatabaseInfo
  environment: string
  cors_origins: string[]
  logging_config: LoggingConfig
} 