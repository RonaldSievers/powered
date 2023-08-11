from leditbe.operations import change_light, LIGHT_XY_RED
from leditbe.tests.conftest import MockedLight


def test_change_light(mocked_light: MockedLight) -> None:
    change_light(mocked_light, 100, LIGHT_XY_RED)
    assert mocked_light.on is True
    assert mocked_light.brightness == 100
    assert mocked_light.transitiontime == 1
    assert mocked_light.xy == LIGHT_XY_RED
