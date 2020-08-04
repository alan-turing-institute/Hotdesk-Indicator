"""Test the error pages."""
import pytest


@pytest.fixture()
def e404_response(client):
    """Get the response from a 404 error."""
    return client.get("/this_route_does_not_exist")


def test_status_code(e404_response):
    """Test the response status."""
    assert e404_response.status_code == 404


def test_contents(e404_response):
    """Test the response data."""
    assert "Not Found" in e404_response.get_data(as_text=True)


def test_title(e404_response):
    """Test the response title."""
    assert (
        "<title>404 Not Found</title>" in e404_response.get_data(as_text=True)
        )
