from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

# IMPORTANT: This import ensures middleware file loads
from app.middleware.org_context import org_context_middleware

# Routers
from app.routers import routes_auth, routes_users, routes_documents

# Database initialization
from app.database.connection import Base, engine

print("🔥 main.py LOADED")


# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="ChainDocs Backend",
    description="Week 1 + Week 2 Backend with JWT, RBAC and Org Scoping",
    version="1.0"
)

# Register CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTER MIDDLEWARE — THIS MUST RUN!
app.middleware("http")(org_context_middleware)
print("🔥 Middleware registered in main.py")


# ROUTES
app.include_router(routes_auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(routes_users.router, prefix="/users", tags=["Users"])
app.include_router(routes_documents.router, prefix="/documents", tags=["Documents"])

print("🔥 Routers registered")


@app.get("/")
def root():
    return {"msg": "Backend is running successfully!"}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="ChainDocs Backend",
        version="1.0.0",
        description="Backend with JWT Auth, RBAC, Org Scoping",
        routes=app.routes,
    )

    # ADD THE BEARER AUTH SECURITY SCHEME
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    # Apply "BearerAuth" to all protected endpoints
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            # skip public paths
            if path.startswith("/auth") or path in ["/", "/docs", "/openapi.json"]:
                continue

            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
