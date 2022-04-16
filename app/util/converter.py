from typing import Union


def number_to_brazilian_real(num: Union[int, float]) -> str:
    currency = f'R$ {float(num):,.2f}'
    currency.replace(',', '*')
    currency.replace('.', ',')
    currency.replace('*', '.')
    return currency
