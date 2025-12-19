print("🔥 ORG CONTEXT MIDDLEWARE LOADED")

from fastapi import Request
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM


async def org_context_middleware(request: Request, call_next):

    path = request.url.path

    # Allow ONLY exact root path
    if path == "/":
        return await call_next(request)

    # Allow auth-related paths
    if path.startswith("/auth"):
        return await call_next(request)

    # Allow Swagger UI & OpenAPI
    if path in ["/docs", "/openapi.json"]:
        return await call_next(request)

    # Debug: print every protected path
    print("🔒 Protected path accessed:", path)

    # Read Auth header
    auth = request.headers.get("authorization")
    print("AUTH HEADER RECEIVED:", auth)

    if not auth:
        return JSONResponse(status_code=401, content={"detail": "Missing authorization header"})

    try:
        scheme, token = auth.split()
        if scheme.lower() != "bearer":
            return JSONResponse(status_code=401, content={"detail": "Invalid auth scheme"})
    except:
        return JSONResponse(status_code=401, content={"detail": "Invalid authorization format"})

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("JWT PAYLOAD:", payload)
    except JWTError as e:
        return JSONResponse(status_code=401, content={"detail": f"Invalid token: {str(e)}"})

    request.state.user = payload
    return await call_next(request)
