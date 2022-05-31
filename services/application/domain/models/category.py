# Standard Python Libraries
from dataclasses import dataclass


@dataclass
class Category:
    category_id: str
    creation_date: str
    update_date: str
    name: str
    slug: str
