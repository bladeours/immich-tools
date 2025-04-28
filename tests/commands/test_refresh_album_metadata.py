import pytest
from unittest.mock import patch
from click.testing import CliRunner
from src.commands.refresh_album_metadata import refresh_album_metadata


@pytest.fixture
def mock_get():
    with patch("src.commands.refresh_album_metadata.send_get") as mock_get:
        yield mock_get


@pytest.fixture
def mock_post():
    with patch("src.commands.refresh_album_metadata.send_post") as mock_post:
        yield mock_post


@pytest.fixture
def runner():
    return CliRunner()


def test_refresh_album_metadata(mock_get, mock_post, runner):
    # Mock API responses
    mock_get.return_value.json.return_value = {
        "albumName": "Test Album",
        "assets": [{"id": "asset1"}, {"id": "asset2"}],
    }
    
    url = "http://test-url.com"
    api_key = "testApiKey"
    album_id = "testAlbumId"
    r = runner.invoke(refresh_album_metadata, ["--api-key", api_key, "--url", url, album_id])

    mock_get.assert_called_once_with(
        path=f"/api/albums/{album_id}",
        url=url,
        api_key=api_key,
    )
    print(r.output)
    print(mock_post.call_args_list)  # Debugging: Check if send_post was called
    print(mock_get.call_args_list)  # Debugging: Check if send_get was called
    # mock_post.assert_any_call()
    mock_post.assert_called_once_with(
        "/api/assets/jobs",
        url,
        api_key,
        {"assetIds": ["asset1", "asset2"], "name": "refresh-metadata"},
    )
