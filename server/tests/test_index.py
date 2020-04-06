"""Tests for the index route."""
import pytest


@pytest.fixture()
def index_response(client):
    """Get the response from the index route."""
    return client.get("/")


def test_status_code(index_response):
    """Test the index response status."""
    assert index_response.status_code == 200


def test_contents(index_response):
    """Test the index response data."""
    assert "Hello world!" in index_response.get_data(as_text=True)
