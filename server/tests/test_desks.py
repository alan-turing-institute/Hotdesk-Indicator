"""Test the desks route."""
import pytest


@pytest.fixture
def desks_response(client):
    """Return the response from the desks route."""
    return client.get("/desks")


def test_status_code(desks_response):
    """Test the desks response status code."""
    assert desks_response.status_code == 200


class TestContents():
    """Test the contents of the response."""

    def test_heading(self, desks_response):
        """Test the page heading."""
        assert "<h1>Desks</h1>" in desks_response.get_data(as_text=True)

    @pytest.mark.parametrize(
        "number,name",
        [("1", "DESK-01"),
         ("2", "DESK-02"),
         ("3", "DESK-03")]
        )
    def test_table_rows(self, desks_response, number, name):
        """Test the booking table rows."""
        row = f"""<tr>
            <th scope="row">{number}</th>
            <td>{name}</td>"""
        assert row in desks_response.get_data(as_text=True)
