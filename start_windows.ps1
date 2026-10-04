<#
.SYNOPSIS
PatchPal Windows Startup Script

This script starts the PatchPal application:
1. Starts the FastAPI backend (http://localhost:8000)
2. Starts the Next.js frontend (http://localhost:3000)

Prerequisites:
- Ollama must be installed with gemma2:2b model
- Python dependencies: pip install -e ".[dev]" in backend/
- Node dependencies: npm install in frontend/
- Default profile: backend/profiles/friend.yaml
#

Write-Host "=== PatchPal Windows Startup ===" -ForegroundColor Cyan
Write-Host ""

# Start Backend
Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Yellow
cd C:\Projects\hacktoberfest26\patchpal\backend
Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -command `"& uvicorn src.patchpal.main:app --reload`"` -WindowStyle Hidden
Write-Host "Backend starting at http://localhost:8000" -ForegroundColor Gray

# Wait for backend to initialize
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "Starting Frontend (Next.js)..." -ForegroundColor Yellow
cd C:\Projects\hacktoberfest26\patchpal\frontend
Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -command `"& npm run dev`"` -WindowStyle Hidden
Write-Host "Frontend starting at http://localhost:3000" -ForegroundColor Gray

Write-Host "" -ForegroundColor Cyan
Write-Host "=== PatchPal is running! ===" -ForegroundColor Cyan
Write-Host "Backend: http://localhost:8000" -ForegroundColor Gray
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Gray
Write-Host ""
Write-Host "Press Ctrl+C to stop this script (servers continue running)." -ForegroundColor Cyan

# Keep script running
Do {
    Start-Sleep -Seconds 30
} While ($true)