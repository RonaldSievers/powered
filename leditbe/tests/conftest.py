import pytest

from leditbe.model import MockedLight, MockedBridge


@pytest.fixture()
def mocked_light() -> MockedLight:
    return MockedLight()


@pytest.fixture()
def mocked_bridge(mocked_light) -> MockedBridge:
    return MockedBridge(mocked_light)
