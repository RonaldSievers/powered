from pydantic_settings import BaseSettings, SettingsConfigDict
from ipaddress import IPv4Address


class HueSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="hue_")
    bridge_ip_address: IPv4Address
    light_name: str
