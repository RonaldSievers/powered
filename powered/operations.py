from requests import request
from powered.model import P1_meter, ConsumptionMetrics
from powered.exceptions import MeterDataParsingException

from typing import Dict, Callable


def _http_handler(endpoint: str) -> Dict:
    api_request = request("GET", endpoint)
    return api_request.json()


def get_metrics_from_p1_meter(
    p1_meter: P1_meter, http_handler: Callable = _http_handler
) -> ConsumptionMetrics:
    api_response = http_handler(p1_meter.endpoint)

    try:
        api_metrics = ConsumptionMetrics(
            active_power_w=api_response["active_power_w"],
            total_power_import_kwh=api_response["total_power_import_kwh"],
            total_power_export_kwh=api_response["total_power_export_kwh"],
        )
    except (ValueError, KeyError) as e:
        raise MeterDataParsingException()

    return api_metrics
