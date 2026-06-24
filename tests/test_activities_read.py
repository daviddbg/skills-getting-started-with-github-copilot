EXPECTED_ACTIVITY_KEYS = {
    "Chess Club",
    "Programming Class",
    "Gym Class",
    "Basketball Team",
    "Soccer Club",
    "Art Studio",
    "Drama Club",
    "Debate Team",
    "Math Olympiad Club",
}


def test_get_activities_returns_expected_shape(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload.keys()) == EXPECTED_ACTIVITY_KEYS
    for activity in payload.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
