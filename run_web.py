"""
MediAlert Pro Web Application Launcher
Runs the Flask application and opens the web dashboard in your default browser.
"""
import os
import sys
import webbrowser
import threading
import time
import socket

# Fix Windows cp1252 encoding issues
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Ensure working directory is the medicine_alert_system folder
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, "medicine_alert_system")
if os.path.exists(app_dir):
    os.chdir(app_dir)
    sys.path.insert(0, app_dir)

try:
    from app import app
except ImportError as e:
    print(f"\n[ERROR] Failed to import application dependencies: {e}")
    print("Please install required libraries by running:")
    print("  pip install flask flask-login apscheduler\n")
    sys.exit(1)

def find_available_port(start=5000, max_attempts=10):
    """Finds an available port starting from 5000."""
    for port in range(start, start + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start

def open_browser(url):
    time.sleep(1.2)
    try:
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    port = find_available_port(5000)
    url = f"http://127.0.0.1:{port}"

    print("\n" + "="*65)
    print("  MediAlert Pro - Clinical Pharmacy Inventory Web System")
    print("="*65)
    print(f"  Server URL: {url}")
    print("  Demo Accounts on Login Screen:")
    print("   - Admin:        admin / admin123")
    print("   - Pharmacist 1: Bhakti / Bhakti@1234")
    print("   - Pharmacist 2: Arpita / Arpita@1234")
    print("="*65)
    print("  Press Ctrl+C in this window to stop the server.\n")
    
    # Open browser automatically in background
    threading.Thread(target=open_browser, args=(url,), daemon=True).start()
    
    try:
        app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)
    except Exception as e:
        print(f"\n[ERROR] Server execution error: {e}")
