from powered.discovery import discover_p1_meter

from zeroconf import ServiceInfo
from powered.model import P1_meter


def test_discover_service(
    mocked_service_info: ServiceInfo, mocked_p1_meter: P1_meter
) -> None:
    device = discover_p1_meter(polling_function=lambda: mocked_service_info)
    assert device == mocked_p1_meter


def test_discover_no_service() -> None:
    device = discover_p1_meter(polling_function=lambda: None)
    assert device is None
