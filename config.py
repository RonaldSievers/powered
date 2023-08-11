from pydantic_settings import BaseSettings, SettingsConfigDict
from ipaddress import IPv4Address

from typing import Optional


class HueSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="hue_")

    bridge_ip_address: Optional[IPv4Address] = None
    light_name: Optional[str] = None
