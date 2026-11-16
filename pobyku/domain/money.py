from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Money:
    amount: Decimal

    @staticmethod
    def from_str(value: str) -> "Money":
        return Money(Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

    @staticmethod
    def zero() -> "Money":
        return Money(Decimal("0.00"))

    def __add__(self, other: "Money") -> "Money":
        return Money((self.amount + other.amount).quantize(Decimal("0.01")))

    def __sub__(self, other: "Money") -> "Money":
        return Money((self.amount - other.amount).quantize(Decimal("0.01")))

    def __mul__(self, count: int) -> "Money":
        return Money((self.amount * Decimal(count)).quantize(Decimal("0.01")))

    def __lt__(self, other: "Money") -> bool:
        return self.amount < other.amount

    def format_pln(self) -> str:
        return f"{self.amount:.2f} zł"
