from typing import Self
from entities.Currency.CurrencyEntity import CurrencyEntity
from exceptions.type_exeptions.PriceException import PriceException


class Price:

    _DIGITS = 2

    def __init__(self, value: int, currency: CurrencyEntity) -> None:
        self._subunits_number = 10 ** self._DIGITS
        print(self._subunits_number)
        self.value = value
        self.currency = currency

    def __repr__(self) -> str:
        return f'Price: value: {self.value}. price: {self.integer}.{self.fractional}{self.currency.symbol}'

    def __add__(self, other: Self) -> Self:
        if self.currency.code != other.currency.code:
            raise PriceException('prices in different currencies cannot be added')

        total_value = self.value + other.value

        return Price(total_value, self.currency)

    def __sub__(self, other: Self) -> Self:
        if self.currency.code != other.currency.code:
            raise PriceException('prices in different currencies cannot be subtracted')

        total_value = self.value - other.value

        return Price(total_value, self.currency)

    @property
    def integer(self) -> int:
        return self.value // self._subunits_number

    @property
    def fractional(self) -> int:
        return self.value % self._subunits_number