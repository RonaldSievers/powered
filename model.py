from pydantic import BaseModel

from requests import request


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

    @property
    def endpoint(self):
        return f"http://{self.server}:{self.port}{self.path}/data"

    @property
    def metrics(self) -> ConsumptionMetrics:
        api_request = request("GET", self.endpoint)
        api_response = api_request.json()
        api_metrics = ConsumptionMetrics(
            active_power_w=api_response["active_power_w"],
            total_power_import_kwh=api_response["total_power_import_kwh"],
        )
        return api_metrics
