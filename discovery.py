from time import sleep
from socket import inet_ntoa

from zeroconf import ServiceBrowser, ServiceListener, Zeroconf, ServiceInfo

from typing import Optional, Union, List, Callable

from model import P1_meter

from log_configuration import logger

HWENERGY_TYPE = "_hwenergy._tcp.local."
TIMEOUT_IN_SECONDS = 5

services_catalogue: List[ServiceInfo] = []


class HWEnergyListener(ServiceListener):
    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        assert isinstance(info, ServiceInfo)
        services_catalogue.append(info)


def _poll_for_services() -> Optional[ServiceInfo]:
    local_tries = 0
    while True:
        if services_catalogue:
            return services_catalogue[0]
        local_tries += 1
        if local_tries > TIMEOUT_IN_SECONDS:
            return None
        logger.info(f"Attempt #{local_tries} in discovering P1 meter..")
        sleep(1)


def _to_ascii(value: Union[str, bytes, None]) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("ascii")
    return value


def discover_p1_meter(
    polling_function: Callable = _poll_for_services,
) -> Optional[P1_meter]:
    services_catalogue.clear()
    zeroconf = Zeroconf()
    listener = HWEnergyListener()
    ServiceBrowser(zeroconf, HWENERGY_TYPE, listener)
    detected_service = polling_function()
    if not detected_service:
        return None

    props = detected_service.properties
    if not props:
        return None

    address = detected_service.addresses[0]
    # Convert an IP address from 32-bit packed binary format to string format
    # We need to convert this as DNS lookup on the private host network doesn't work in the docker container
    ip_address = inet_ntoa(address)

    return P1_meter(
        server=ip_address,
        port=detected_service.port or 0,
        api_enabled=bool(props[b"api_enabled"]),
        path=_to_ascii(props[b"path"]),
        serial=_to_ascii(props[b"serial"]),
        product_type=_to_ascii(props[b"product_type"]),
        product_name=_to_ascii(props[b"product_name"]),
    )
