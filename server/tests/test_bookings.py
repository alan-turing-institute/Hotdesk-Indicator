"""Test the bookings route."""
import pytest


@pytest.fixture
def bookings_response(client):
    """Get the reponse from the bookings route."""
    return client.get("/bookings")


def test_status_code(bookings_response):
    """Test the bookings response status code."""
    assert bookings_response.status_code == 200


class TestContents():
    """Test the contents of the response."""

    def test_heading(self, bookings_response):
        """Test the page heading."""
        assert "<h1>Bookings</h1>" in bookings_response.get_data(as_text=True)

    @pytest.mark.parametrize(
        "number,desk_id,name,from_when,until_when",
        [("1", "DESK-01", "Harry Lime", "09:00", "17:00"),
         ("2", "DESK-02", "Kaiser Söze", "09:00", "12:00"),
         ("3", "DESK-02", "Sam Spade", "13:00", "16:00")]
        )
    def test_table_rows(self, bookings_response, number, desk_id, name,
                        from_when, until_when):
        """Test the booking table rows."""
        row = f"""<tr>
            <th scope="row">{number}</th>
            <td>{desk_id}</td>
            <td>{name}</td>
            <td>{from_when}</td>
            <td>{until_when}</td>
            <td>No</td>
        </tr>"""
        assert row in bookings_response.get_data(as_text=True)

    def test_missing_desk(self, bookings_response):
        """Ensure DESK-03 is not present as it is not booked."""
        assert "DESK-03" not in bookings_response.get_data(as_text=True)
