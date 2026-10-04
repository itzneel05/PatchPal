#!/bin/bash
# =============================================================================
# PatchPal Linux Startup Script
# =============================================================================
# Starts the PatchPal application:
# 1. FastAPI backend (http://localhost:8000)
# 2. Next.js frontend (http://localhost:3000)
#
# Prerequisites:
# - Ollama with gemma2:2b model
# - Python deps: pip install -e ".[dev]" in backend/
# - Node deps: npm install in frontend/
# - Profile: backend/profiles/friend.yaml
# =============================================================================

set -e

echo "=== PatchPal Linux Startup ==="

# Start Backend
echo "Starting Backend (FastAPI)..."
cd /Projects/hacktoberfest26/patchpal/backend
nohup uvicorn src.patchpal.main:app --reload > /tmp/patchpal_backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"
echo "Backend: http://localhost:8000"

# Wait for backend to start
sleep 3

# Start Frontend
echo "Starting Frontend (Next.js)..."
cd /Projects/hacktoberfest26/patchpal/frontend
nohup npm run dev > /tmp/patchpal_frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Frontend PID: $FRONTEND_PID"
echo "Frontend: http://localhost:3000"

# Display status
echo ""
echo "PatchPal is now running!"
echo "To view logs: tail -f /tmp/patchpal_backend.log /tmp/patchpal_frontend.log"
echo "Backend PID: $BACKEND_PID | Frontend PID: $FRONTEND_PID"
echo ""

# Keep script running to maintain process oversight
trap "echo 'Stopping PatchPal...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit 0" INT TERM
while true; do
    sleep 60
    if ! kill -0 $BACKEND_PID 2>/dev/null; then
        echo "Warning: Backend process died. Check /tmp/patchpal_backend.log"
    fi
    if ! kill -0 $FRONTEND_PID 2>/dev/null; then
        echo "Warning: Frontend process died. Check /tmp/patchpal_frontend.log"
    fi
done