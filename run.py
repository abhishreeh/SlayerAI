"""
Launch script for Dark Pattern Slayer & Bureaucracy Navigator (AdvocateOS)
"""

import uvicorn
import os
import sys

# Configure UTF-8 encoding for Windows terminals
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure current directory is in PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[SlayerAI] Starting Dark Pattern Slayer & Bureaucracy Navigator on http://127.0.0.1:{port}")
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=False)
