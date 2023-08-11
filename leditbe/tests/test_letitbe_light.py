from leditbe.light import find_light
from ipaddress import IPv4Address

from leditbe.tests.conftest import MockedLight, MockedBridge


def test_find_light(mocked_bridge: MockedBridge, mocked_light: MockedLight) -> None:
    light = find_light("TestLight", IPv4Address("192.168.2.1"), lambda x: mocked_bridge)
    assert light == mocked_light
