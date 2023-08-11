import os

from phue import Bridge, Light, PhueRegistrationException
from ipaddress import IPv4Address

from typing import Optional, Callable
from leditbe.log_configuration import logger

CONFIG_PATH = os.path.join(os.getcwd(), "storage/.python_hue")


def _bridge_by_ipaddress(ip_address: IPv4Address) -> Bridge:
    bridge = Bridge(str(ip_address), config_file_path=CONFIG_PATH)
    logger.info("Trying to connect to the HUE bridge.. ")
    try:
        bridge.connect()
    except PhueRegistrationException:
        logger.error(
            "This computer has not been registered with the Hue bridge yet. Press the button on the bridge and then rerun this app within 30 seconds."
        )
        exit(1)
    return bridge


def find_light(
    light_name: str,
    bridge_ip_address: IPv4Address,
    brigde_handler: Optional[Callable] = None,
) -> Optional[Light]:
    brigde_handler = brigde_handler or _bridge_by_ipaddress
    bridge = brigde_handler(bridge_ip_address)
    light_names = bridge.get_light_objects("name")

    if light_name not in light_names:
        logger.error(
            f'Unable to find the target light. Available lights: {", ".join(light_names.keys())}. Make sure the name is correctly spelled, and case sensitivity is taken into account.'
        )
        return None

    found_light = light_names[light_name]
    logger.info(f"Succesfully found light {found_light}")
    return found_light
