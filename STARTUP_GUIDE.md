# PatchPal Manual Startup Guide

If the automatic scripts have issues due to shell quoting, use these manual steps:

## Step 1: Start the Backend (Python/FastAPI)

**Open a Command Prompt (cmd.exe)** and run:

```cmd
cd C:\Projects\hacktoberfest26\patchpal\backend
pip install -e ".[dev]"  (if not already installed)
uvicorn src.patchpal.main:app --reload
```

You should see:
```
INFO:     Started server [uvicorn:app] on http://127.0.0.1:8000
INFO:     Started reloader process [1232] watching .\src
```

The backend will be available at `http://localhost:8000`

## Step 2: Start the Frontend (Next.js)

**Open a SEPARATE Command Prompt** and run:

```cmd
cd C:\Projects\hacktoberfest26\patchpal\frontend
npm install  (if first time)
npm run dev
```

You should see:
```
  ▲  Natal is building client...
  ✓ Attempted to compile types with the TypeScript compiler.
  ✓ Reloading in 1.0s.
```

The frontend will be available at `http://localhost:3000`

## Step 3: Verify Both Are Running

Open your web browser and visit:
- `http://localhost:3000` - You should see the PatchPal dashboard
- `http://localhost:8000/api/health` - Should return `{"status":"ok","message":"PatchPal API is running"}`

## Step 4: Use the Application

The dashboard should load, showing:
- Your friend's name (from the profile)
- AI-generated security digest
- Relevant vulnerability cards filtered by their tech stack
- Option to refresh to fetch new data

## Step 4: Stop the Servers

In each command prompt window, press `Ctrl+C` to stop the server.

## Troubleshooting

### "Failed to fetch digest" error:
1. Ensure the backend (port 8000) is running before the frontend (port 3000)
2. Check that both servers are running in separate command prompt windows
3. Verify the profile file exists: `backend\profiles\friend.yaml`

### Port already in use:
If ports 8000 or 3000 are already occupied, modify the ports in:
- `backend\src\patchpal\main.py` (change `port=8000`)
- `frontend\package.json` (change the dev script port)

### No vulnerabilities showing:
- Check that the friend profile `backend\profiles\friend.yaml` has tech_stack entries
- The AI needs at least some tech stack items to filter against
- Try the "Refresh" button to fetch new RSS feeds

## Project Structure Reference

```
patchpal/
├── backend/          (start here first)
│   └── uvicorn src.patchpal.main:app --reload
├── frontend/         (start second)
│   └── npm run dev
└── profiles/
    └── friend.yaml   (default: Parth's tech stack)
```

## Need Help?

- Check that both command prompts are open and the servers are running
- Verify Python and Node.js are installed and in your PATH
- Ensure `backend\profiles\friend.yaml` exists with a name and tech_stack list
- All 17+ pytest tests pass: `cd backend && pytest`