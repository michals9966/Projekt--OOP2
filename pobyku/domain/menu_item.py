from dataclasses import dataclass
from .money import Money


@dataclass(frozen=True)
class MenuItem:
    id: str
    name: str
    category: str
    price: Money
