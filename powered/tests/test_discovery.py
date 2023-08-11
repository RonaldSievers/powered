from powered.discovery import discover_p1_meter


def test_discover_service(mocked_service_info, mocked_p1_meter) -> None:
    device = discover_p1_meter(polling_function=lambda: mocked_service_info)
    assert device == mocked_p1_meter


def test_discover_no_service() -> None:
    device = discover_p1_meter(polling_function=lambda: None)
    assert device is None
