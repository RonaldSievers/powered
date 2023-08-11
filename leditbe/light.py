from phue import Bridge, Light, PhueRegistrationException

from typing import Optional
from leditbe.log_configuration import logger


def find_light(light_name: str, bridge_ip_address: str) -> Optional[Light]:
    b = Bridge(bridge_ip_address)

    logger.info("Trying to connect to the HUE bridge.. ")
    try:
        b.connect()
    except PhueRegistrationException as e:
        logger.error(
            "This computer has not been registered with the Hue bridge yet. Press the button on the bridge and then rerun this app within 30 seconds."
        )
        exit(1)

    light_names = b.get_light_objects("name")

    if light_name not in light_names:
        logger.error(
            "Unable to find the target light. Make sure the name is correctly spelled, and case sensitivity is taken into account."
        )
        return None

    found_light = light_names[light_name]
    logger.info(f"Succesfully found light {found_light}")
    return found_light
