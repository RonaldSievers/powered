from zeroconf import ServiceInfo
import random


def demo_poll_for_services() -> ServiceInfo:
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


def demo_http_handler(endpoint: str) -> dict:
    assert endpoint
    return dict(
        active_power_w=random.randrange(-3000, 3000),
        total_power_import_kwh=9412.12,
        total_power_export_kwh=4123.33,
    )
