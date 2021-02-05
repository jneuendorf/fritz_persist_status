from dataclasses import dataclass
from typing import Iterable

from .user_settings import settings as user_settings


@dataclass
class Settings:
    attrs: Iterable[str] = ('is_connected', 'is_linked',
                            'str_transmission_rate', 'str_uptime')
    output_file: str = './fritz_status.csv'
    error_file: str = './fritz_status.log'


settings = Settings(**user_settings)
