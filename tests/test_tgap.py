import subprocess
import sys


def test_help() -> None:
    """Test that the `tgap` module's `--help` option can be invoked successfully."""
    try:
        subprocess.check_call([sys.executable, "-m", "tgap", "--help"])
    except subprocess.CalledProcessError as e:
        print(f"Test failed: {e}")
        raise
