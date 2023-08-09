from discovery import discover_service
from zeroconf import ServiceInfo

from model import PowerDevice

def test_discover_service(service_info: ServiceInfo, power_device: PowerDevice) -> None:
    device = discover_service(polling_function=lambda: service_info)
    assert device == power_device


def test_discover_no_service() -> None:
    device = discover_service(polling_function=lambda: None)
    assert device is None
