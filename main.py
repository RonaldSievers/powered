from time import sleep
import click

from log_configuration import logger
from powered.discovery import discover_p1_meter
from powered.operations import get_metrics_from_p1_meter
from powered.demo import demo_http_handler, demo_poll_for_services

from leditbe.light import find_light

# HUE CONFIG
HUE_BRIDGE_IP_ADDRESS = "192.168.2.1"
HUE_LIGHT_NAME = "Wand"  ## case sensitive


@click.command()
@click.option("--demo", default=False, is_flag=True, help="If demo mode is enabled")
def main(demo):
    logger.info(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )

    light = find_light(HUE_LIGHT_NAME, HUE_BRIDGE_IP_ADDRESS)
    if not light:
        logger.error(
            f"""Unable to find the target light {HUE_LIGHT_NAME} on hue bridge with ip {HUE_BRIDGE_IP_ADDRESS}. 
            You might need to push the HUE bridge sync button first."""
        )
        exit(1)

    from leditbe.operations import blink

    blink(light)

    p1_meter = discover_p1_meter(
        polling_function=demo_poll_for_services if demo else None
    )
    if not p1_meter:
        logger.error("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    logger.info(f"P1 Meter found ({p1_meter})")

    # for now, lets loop until infinity :D
    while True:
        metrics = get_metrics_from_p1_meter(
            p1_meter=p1_meter, http_handler=demo_http_handler if demo else None
        )
        logger.info(f"Metrics retrieved: {metrics}")
        sleep(1)


if __name__ == "__main__":
    main()
