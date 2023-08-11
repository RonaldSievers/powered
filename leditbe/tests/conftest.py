import pytest

from phue import Bridge


class MockedBridge:
    def __init__(self, light):
        self.light = light

    def get_light_objects(self, mode: str):
        return {"TestLight": self.light}


class MockedLight:
    on: bool = False
    transitiontime: int = 1
    brightness: int = 0
    xy = [0, 0]


@pytest.fixture()
def mocked_light() -> MockedLight:
    return MockedLight()


@pytest.fixture()
def mocked_bridge(mocked_light) -> MockedBridge:
    return MockedBridge(mocked_light)
