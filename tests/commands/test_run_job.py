import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from src.commands.run_job import run_job


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def mock_logger():
    with patch("src.commands.run_job.log") as mock_log:
        yield mock_log


@pytest.fixture
def mock_send_put():
    with patch("src.commands.run_job.send_put") as mock_put:
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success"}
        mock_put.return_value = mock_response
        yield mock_put


def test_run_job_success(runner, mock_logger, mock_send_put):
    api_key = "test_api_key"
    url = "http://test-url.com"
    job_name = "thumbnailGeneration"

    result = runner.invoke(run_job, ["--api-key", api_key, "--url", url, job_name])

    # Assertions
    assert result.exit_code == 0
    mock_logger.debug.assert_any_call(f"immich url: {url}")
    mock_send_put.assert_called_once_with(
        path=f"/api/jobs/{job_name}", url=url, api_key=api_key, data={"command": "start", "force": True}
    )
    mock_logger.debug.assert_any_call(f"running job: {job_name}")
