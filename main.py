from discovery import discover_service


def main():
    print(
        "Powered .. by Ronald Sievers. Open source so feel free to modify and copy as much you'd like."
    )
    print("Detecting HomeWizard P1 Meter in your network ..")
    device = discover_service()
    if not device:
        print("Sorry, unable to locate the device. Are you on the same network?")
        exit(1)
    print(f"Device located ({device})")
    print(f"Metrics retrieved: {device.metrics}")


if __name__ == "__main__":
    main()
