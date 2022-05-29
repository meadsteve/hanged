# Standard Python Libraries
from datetime import datetime


def date_time_str_to_iso_format(date_time_str: str) -> str:
    return datetime.strptime(date_time_str, "%Y-%m-%d").isoformat()
