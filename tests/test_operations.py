from operations import get_metrics_from_p1_meter


def test_get_metrics_from_p1_meter(
    mocked_p1_meter, mocked_api_response, mocked_consume_metrics
):
    metrics = get_metrics_from_p1_meter(
        mocked_p1_meter, lambda endpoint: mocked_api_response
    )
    assert metrics == mocked_consume_metrics
