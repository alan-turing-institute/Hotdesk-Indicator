"""Test the book route."""
from datetime import datetime, timedelta


def test_book_response(client):
    """Test the booking route."""
    response = client.get("/book")
    assert "<h1>Book a Desk" in response.get_data(as_text=True)


def test_book(client, today):
    """Test booking a desk."""
    current_time = datetime.now()
    from_when = current_time.strftime("%H:%M")
    until_when = (current_time + timedelta(minutes=1)).strftime("%H:%M")

    response = client.post(
        "/book",
        data={
            "name": "Richard Hannay",
            "desk": 3,
            "date": today,
            "from_when": from_when,
            "until_when": until_when
            },
        follow_redirects=True
        )

    assert response.status_code == 200
    assert "Your desk is booked!" in response.get_data(as_text=True)

    row = f"""<tr>
            <th scope="row">4</th>
            <td>DESK-03</td>
            <td>Richard Hannay</td>
            <td>{today.strftime("%Y-%m-%d")}</td>
            <td>{from_when}</td>
            <td>{until_when}</td>
            <td>Yes</td>
        </tr>"""
    assert row in response.get_data(as_text=True)


def test_book_inactive(client, today):
    """Test booking a desk."""
    current_time = datetime.now()
    from_when = (current_time - timedelta(minutes=1)).strftime("%H:%M")
    until_when = current_time.strftime("%H:%M")

    response = client.post(
        "/book",
        data={
            "name": "Richard Hannay",
            "desk": 3,
            "date": today,
            "from_when": from_when,
            "until_when": until_when
            },
        follow_redirects=True
        )

    assert response.status_code == 200
    assert "Your desk is booked!" in response.get_data(as_text=True)

    row = f"""<tr>
            <th scope="row">4</th>
            <td>DESK-03</td>
            <td>Richard Hannay</td>
            <td>{today.strftime("%Y-%m-%d")}</td>
            <td>{from_when}</td>
            <td>{until_when}</td>
            <td>No</td>
        </tr>"""
    assert row in response.get_data(as_text=True)
