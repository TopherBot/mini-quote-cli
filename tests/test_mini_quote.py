import subprocess
import sys

def test_cli_returns_a_quote():
    # Run the module as a script
    result = subprocess.run([sys.executable, '-m', 'mini_quote'], capture_output=True, text=True)
    assert result.returncode == 0
    output = result.stdout.strip()
    # Ensure output looks like a quote (contains a dash and a quotation mark)
    assert "–" in output
    assert len(output) > 10
