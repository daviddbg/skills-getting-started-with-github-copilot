from urllib.parse import quote

from src.app import activities


def test_unregister_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    encoded_activity = quote(activity_name, safe="")
    url = f"/activities/{encoded_activity}/participants"

    # Act
    response = client.delete(url, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregister_non_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.enrolled@mergington.edu"
    encoded_activity = quote(activity_name, safe="")
    url = f"/activities/{encoded_activity}/participants"

    # Act
    response = client.delete(url, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_missing_activity_returns_404(client):
    # Arrange
    activity_name = "Astronomy Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name, safe="")
    url = f"/activities/{encoded_activity}/participants"

    # Act
    response = client.delete(url, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
