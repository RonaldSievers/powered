from log_configuration import logger
from discovery import discover_service


def main():
    logger.info(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )
    logger.info("Detecting HomeWizard P1 Meter in your network ..")
    device = discover_service()
    if not device:
        logger.error("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    logger.info(f"Device located ({device})")
    logger.info(f"Metrics retrieved: {device.metrics}")


if __name__ == "__main__":
    main()
