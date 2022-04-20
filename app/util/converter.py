from typing import Union


def number_to_brazilian_real(num: Union[int, float]) -> str:
    br_currency = f'R$ {float(num):,.2f}'
    return br_currency.replace(',', '*').replace('.', ',').replace('*', '.')
