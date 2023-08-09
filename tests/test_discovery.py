from discovery import discover_service
from typing import Optional
from zeroconf import ServiceInfo
from model import PowerDevice


def _mocked_service_info() -> ServiceInfo:
    return ServiceInfo(
        addresses=[b"\xc0\xa8V\xf9"],
        host_ttl=120,
        name="p1meter-0a4066._hwenergy._tcp.local.",
        other_ttl=4500,
        port=80,
        priority=0,
        properties={
            b"api_enabled": b"1",
            b"path": b"/api/v1",
            b"product_name": b"P1 meter",
            b"product_type": b"HWE-P1",
            b"serial": b"5c2faf0a4066",
        },
        server="p1meter-0A4066.local.",
        type_="_hwenergy._tcp.local.",
        weight=0,
    )


def _mocked_poll_for_services() -> Optional[ServiceInfo]:
    return _mocked_service_info()


def test_discover_service() -> None:
    device = discover_service(polling_function=_mocked_poll_for_services)

    assert isinstance(device, PowerDevice)
    assert device.server == "192.168.86.249"
    assert device.port == 80
    assert device.api_enabled == True
    assert device.path == "/api/v1"
    assert device.serial == "5c2faf0a4066"
    assert device.product_type == "HWE-P1"
    assert device.product_name == "P1 meter"


def test_discover_no_service() -> None:
    device = discover_service(polling_function=lambda: None)
    assert device is None
