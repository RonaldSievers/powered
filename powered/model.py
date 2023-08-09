from pydantic import BaseModel


class ConsumptionMetrics(BaseModel):
    active_power_w: int
    total_power_import_kwh: float
    total_power_export_kwh: float


class P1_meter(BaseModel):
    server: str
    port: int
    api_enabled: bool
    path: str
    serial: str
    product_type: str
    product_name: str

    @property
    def endpoint(self) -> str:
        return f"http://{self.server}:{self.port}{self.path}/data"
