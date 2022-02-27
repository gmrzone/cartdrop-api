
import pytest


@pytest.fixture
def temp_fixture():
    print("Running Fixture")
    return 1