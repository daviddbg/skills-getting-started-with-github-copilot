import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def isolate_activities_state():
    snapshot = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(snapshot)
