import pytest
from zeroconf import ServiceInfo
from model import P1_meter


@pytest.fixture()
def service_info():
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


@pytest.fixture()
def power_device(service_info):
    return P1_meter(
        server="192.168.86.249",
        port=80,
        api_enabled=True,
        path="/api/v1",
        serial="5c2faf0a4066",
        product_type="HWE-P1",
        product_name="P1 meter",
    )
