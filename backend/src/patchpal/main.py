from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from patchpal.api.routes import router as api_router

app = FastAPI(
    title="PatchPal API",
    description="Security Threat Digest API for a Friend",
    version="0.1.0"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "PatchPal API is running"}
