"""
Middleware for logging API calls and responses
"""
import logging
import time
import json
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message

logger = logging.getLogger(__name__)

class APILoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging API requests and responses
    Logs method, path, status code, duration, user, and payload
    """
    async def set_body(self, request: Request):
        """Read and store request body"""
        receive_ = await request._receive()

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Start timing
        start_time = time.time()
        
        # Get request body
        await self.set_body(request)
        body = await request.body()
        
        # Get user information
        user = "anonymous"
        if "authorization" in request.headers:
            # Extract username from JWT if present
            try:
                from ..core.security import decode_token
                token = request.headers["authorization"].split(" ")[1]
                payload = decode_token(token)
                user = payload.get("sub", "unknown")
            except Exception:
                user = "invalid_token"

        # Log request
        logger.info(
            "API Request | %s | %s | User: %s | Body: %s",
            request.method,
            request.url.path,
            user,
            body.decode() if body else "No body"
        )

        # Process request
        response = await call_next(request)
        
        # Calculate duration
        duration = time.time() - start_time

        # Get response body
        response_body = b""
        async for chunk in response.body_iterator:
            response_body += chunk

        # Log response
        logger.info(
            "API Response | %s | %s | Status: %d | Duration: %.2fs | User: %s | Body: %s",
            request.method,
            request.url.path,
            response.status_code,
            duration,
            user,
            response_body.decode()
        )

        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        ) 