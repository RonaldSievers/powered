from discovery import discover_p1_meter
from zeroconf import ServiceInfo

from model import P1_meter


def test_discover_service(service_info: ServiceInfo, power_device: P1_meter) -> None:
    device = discover_p1_meter(polling_function=lambda: service_info)
    assert device == power_device


def test_discover_no_service() -> None:
    device = discover_p1_meter(polling_function=lambda: None)
    assert device is None
