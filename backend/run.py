"""
Application runner script.
Configures and starts the uvicorn server.
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_config=None,  # Use application's logging config
    ) 