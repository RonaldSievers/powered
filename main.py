import logging

import click
from time import sleep

import powered  # handles communication with p1 meter
import ledastic  # handles communication with led strip


from log_configuration import logger


MAX_POWERBAR = 72
WATT_PER_BAR = 50  # so
MAX_WATT_VALUE = MAX_POWERBAR * WATT_PER_BAR


@click.command()
@click.option("--demo", default=False, is_flag=True, help="If demo mode is enabled")
def main(demo):
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
    powerbar.boot_up()

    # while True:
    #     for n in range(-MAX_POWERBAR, MAX_POWERBAR):
    #         powerbar.change_to(n)
    #         sleep(0.05)
    #
    #     for n in reversed(range(-MAX_POWERBAR, MAX_POWERBAR)):
    #         powerbar.change_to(n)
    #         sleep(0.05)

    # for now, lets loop until infinity :D
    while True:
        try:
            metrics = powered.get_metrics_from_p1_meter(
                p1_meter=p1_meter,
                http_handler=powered.demo_http_handler if demo else None,
            )
        except powered.MeterDataConnectionErrorException as e:
            logging.warning(
                f"Unable to retrieve metrisc due to connection issues ({e}). Pausing for 5 seconds."
            )
            ledastic.blink(ledastic.COLOR_BLUE, 5)
            sleep(2)
            continue

        actual_brigntness = max(
            MAX_POWERBAR * -1,
            min(MAX_POWERBAR, int(metrics.active_power_w / WATT_PER_BAR)),
        )

        # rest = abs(metrics.active_power_w) - (abs(actual_brigntness) * WATT_PER_BAR)

        powerbar.change_to(actual_brigntness)

        logger.info(
            f"Metrics retrieved: {metrics}, actual brightness: {actual_brigntness}"
        )

        sleep(1)


if __name__ == "__main__":
    main()
