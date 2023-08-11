import click
from time import sleep

import powered  # handles communication with p1 meter
import leditbe  # handles communication with hue bridge

from log_configuration import logger

# HUE CONFIG
from config import HueSettings

app_config = HueSettings()

if not app_config.light_name or not app_config.bridge_ip_address:
    logger.error("Missing environment configuration. Check the manual.")
    exit(1)


@click.command()
@click.option("--demo", default=False, is_flag=True, help="If demo mode is enabled")
def main(demo):
    logger.info(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )

    logger.info(
        f"Connecting to bridge at {app_config.bridge_ip_address}, for light '{app_config.light_name}'"
    )

    light = leditbe.find_light(app_config.light_name, app_config.bridge_ip_address)
    if not light:
        logger.error(
            f"""Unable to find the target light {app_config.light_name} on hue bridge with ip {app_config.bridge_ip_address}. 
            You might need to push the HUE bridge sync button first."""
        )
        exit(1)

    leditbe.blink(light)

    p1_meter = powered.discover_p1_meter(
        polling_function=powered.demo_poll_for_services if demo else None
    )
    if not p1_meter:
        logger.error("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    logger.info(f"P1 Meter found ({p1_meter})")

    # for now, lets loop until infinity :D
    while True:
        metrics = powered.get_metrics_from_p1_meter(
            p1_meter=p1_meter, http_handler=powered.demo_http_handler if demo else None
        )

        max_value = 3000
        max_brightness = 255
        value = min(max_value, abs(metrics.active_power_w))
        perc_value = value / max_value
        actual_brigntness = int(max_brightness * perc_value)

        if metrics.active_power_w < 0:
            # producing energy
            leditbe.to_green(light, actual_brigntness)
        else:
            # consuming energy
            leditbe.to_red(light, actual_brigntness)

        logger.info(
            f"Metrics retrieved: {metrics}, actual brightness: {actual_brigntness}"
        )

        sleep(1)


if __name__ == "__main__":
    main()
