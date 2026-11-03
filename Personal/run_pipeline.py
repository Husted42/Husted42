import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    # Fetch Habitica history
    subprocess.run(
        [sys.executable, str(ROOT / "src" / "get_habitica_history.py")],
        check=True,
        cwd=ROOT,
    )

    # Start Streamlit
    subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(ROOT / "pages" / "test.py")],
        check=True,
        cwd=ROOT,
    )


if __name__ == "__main__":
    main()
