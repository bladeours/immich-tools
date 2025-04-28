from click.testing import CliRunner
from src.commands.version import version
import src


def test_version_command():
    runner = CliRunner()
    result = runner.invoke(version)
    assert result.exit_code == 0
    assert result.output.strip() == src.__version__
