from app.util.converter import number_to_brazilian_real

NUMBER_OF_TRACES = 60


def monthly_report(month: str,
                   stock: int,
                   base_cost: float,
                   total_cost: float,
                   num_units_purchased_month: str,
                   num_units_sold_month: int,
                   num_units_sold_year: int,
                   monthly_gross_revenue: float,
                   monthly_net_revenue: float,
                   annual_net_revenue: float,
                   product_value: float) -> None:
    print('-' * NUMBER_OF_TRACES)
    print(f'{month.upper()}')
    print(f'• Unidades em estoque: {stock} (+ {num_units_purchased_month} unidades adquiridas)')
    print(f'• Unidades vendidas no mês: {num_units_sold_month}')
    print(f'• Unidades vendidas no ano: {num_units_sold_year}')
    print(f'• Custo unitário de aquisição: {number_to_brazilian_real(base_cost)}')
    print(f'• Custo total de aquisição: {number_to_brazilian_real(total_cost)}')
    print(f'• Valor do produto: {number_to_brazilian_real(product_value)}')
    print(f'• Faturamento bruto mensal: {number_to_brazilian_real(monthly_gross_revenue)}')
    print(f'• Faturamento liquído mensal: {number_to_brazilian_real(monthly_net_revenue)}')
    print(f'• Faturamento liquído anual: {number_to_brazilian_real(annual_net_revenue)}')


def annual_report(stock: int,
                  total_purchased: int,
                  total_sale: int,
                  total_cost: float,
                  gross_revenue: float,
                  net_revenue: float,
                  break_even_month: str) -> None:
    print('-' * NUMBER_OF_TRACES)
    print(f'\nRELATÓRIO ANUAL:\n')
    print(f'• Unidades em estoque: {stock}')
    print(f'• Total de produtos comprados: {total_purchased}')
    print(f'• Total de vendas: {total_sale}')
    print(f'• Investimento total: {number_to_brazilian_real(total_cost)}')
    print(f'• Faturamento bruto: {number_to_brazilian_real(gross_revenue)}')
    print(f'• Lucro total: {number_to_brazilian_real(net_revenue)}')
    print(f'• Mês do break even point: {break_even_month}\n')
