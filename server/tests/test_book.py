"""Test the book route."""


def test_book_response(client):
    """Test the booking route."""
    response = client.get("/book")
    assert "<h1>Book a Desk" in response.get_data(as_text=True)


def test_book(client):
    """Test booking a desk."""
    response = client.post(
        "/book",
        data={
            "name": "Richard Hannay",
            "desk": 3,
            "from_when": "10:30",
            "until_when": "14:15"
            },
        follow_redirects=True
        )

    assert response.status_code == 200
    assert "Your desk is booked!" in response.get_data(as_text=True)

    row = """<tr>
            <th scope="row">4</th>
            <td>DESK-03</td>
            <td>Richard Hannay</td>
            <td>10:30</td>
            <td>14:15</td>
        </tr>"""
    assert row in response.get_data(as_text=True)
