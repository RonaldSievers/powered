from pydantic import BaseModel

from requests import request

from exceptions import MeterDataParsingException


class ConsumptionMetrics(BaseModel):
    active_power_w: int
    total_power_import_kwh: float


class PowerDevice(BaseModel):
    server: str
    port: int
    api_enabled: bool
    path: str
    serial: str
    product_type: str
    product_name: str

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.model_dump() == other.model_dump()
        raise Exception("Trying to compare two different models")

    @property
    def endpoint(self):
        return f"http://{self.server}:{self.port}{self.path}/data"

    @property
    def metrics(self) -> ConsumptionMetrics:
        api_request = request("GET", self.endpoint)
        api_response = api_request.json()
        try:
            api_metrics = ConsumptionMetrics(
                active_power_w=api_response["active_power_w"],
                total_power_import_kwh=api_response["total_power_import_kwh"],
            )
        except (ValueError, KeyError) as e:
            raise MeterDataParsingException()

        return api_metrics
