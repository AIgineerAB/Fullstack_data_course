import subprocess
from pathlib import Path

def run_dashboard():
    dashboard_path = Path(__file__).parent / "dashboard.py"
    subprocess.run(["streamlit", "run", dashboard_path])

if __name__ == '__main__':
    run_dashboard()
