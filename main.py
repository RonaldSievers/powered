import click
from time import sleep

import powered  # handles communication with p1 meter
import ledastic  # handles communication with led strip


from log_configuration import logger

MAX_WATT_VALUE = 3000
MAX_POWERBAR = 30


@click.command()
@click.option("--demo", default=False, is_flag=True, help="If demo mode is enabled")
def main(demo):
    demo = True
    logger.info(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )

    p1_meter = powered.discover_p1_meter(
        polling_function=powered.demo_poll_for_services if demo else None
    )
    if not p1_meter:
        logger.error("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    logger.info(f"P1 Meter found ({p1_meter})")

    powerbar = ledastic.PowerBar()

    # for now, lets loop until infinity :D
    while True:
        metrics = powered.get_metrics_from_p1_meter(
            p1_meter=p1_meter, http_handler=powered.demo_http_handler if demo else None
        )

        value = min(MAX_WATT_VALUE, abs(metrics.active_power_w))
        perc_value = value / MAX_WATT_VALUE
        actual_brigntness = int(MAX_POWERBAR * perc_value)

        if metrics.active_power_w < 0:
            actual_brigntness = actual_brigntness * -1
        powerbar.change_to(actual_brigntness)

        logger.info(
            f"Metrics retrieved: {metrics}, actual brightness: {actual_brigntness}"
        )

        sleep(1)


if __name__ == "__main__":
    main()
