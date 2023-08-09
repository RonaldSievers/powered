from time import sleep

from powered.log_configuration import logger
from powered.discovery import discover_p1_meter
from powered.operations import get_metrics_from_p1_meter


def main():
    logger.info(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )
    p1_meter = discover_p1_meter()
    if not p1_meter:
        logger.error("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    logger.info(f"P1 Meter found ({p1_meter})")

    # for now, lets loop until infinity :D
    while True:
        logger.info(f"Metrics retrieved: {get_metrics_from_p1_meter(p1_meter)}")
        sleep(1)


if __name__ == "__main__":
    main()
