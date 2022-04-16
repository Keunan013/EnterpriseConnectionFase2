from app.operation.create_report import monthly_report, annual_report

MONTHS = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
NUMBER_OF_MONTHS = len(MONTHS)
BASE_COST_PER_MONTH = [30.0, 25.0, 35.0, 43.0, 32.0, 32.0, 32.0, 34.0, 45.0, 30.0, 33.0, 35.0]
NUMBER_OF_SALES_PER_MONTH = [225, 300, 333, 352, 145, 842, 144, 752, 520, 222, 127, 333]
PRODUCT_VALUE = 50.0
INITIAL_STOCK = 1000


def fill_out_reports() -> None:
    annual_cost = 0.0
    annual_gross_revenue = 0.0
    annual_net_revenue = 0.0
    num_units_sold_year = 0
    num_units_purchased_year = 0
    stock = 0
    break_even_month = None
    for i in range(NUMBER_OF_MONTHS):
        num_units_sold_month = NUMBER_OF_SALES_PER_MONTH[i]
        num_units_purchased_month = num_units_sold_month if (i != 0) else INITIAL_STOCK + num_units_sold_month
        num_units_purchased_year += num_units_purchased_month
        base_cost = BASE_COST_PER_MONTH[i]
        stock = INITIAL_STOCK + num_units_sold_month
        monthly_cost = num_units_sold_month * base_cost if (i != 0) else stock * base_cost
        annual_cost += monthly_cost
        monthly_gross_revenue = NUMBER_OF_SALES_PER_MONTH[i] * PRODUCT_VALUE
        monthly_net_revenue = monthly_gross_revenue - monthly_cost
        annual_gross_revenue += monthly_gross_revenue
        annual_net_revenue += monthly_net_revenue
        num_units_sold_year += num_units_sold_month
        monthly_report(month=MONTHS[i],
                       stock=stock,
                       base_cost=base_cost,
                       total_cost=monthly_cost,
                       num_units_purchased_month=num_units_purchased_month,
                       num_units_sold_month=num_units_sold_month,
                       num_units_sold_year=num_units_sold_year,
                       monthly_gross_revenue=monthly_gross_revenue,
                       monthly_net_revenue=monthly_net_revenue,
                       annual_net_revenue=annual_net_revenue,
                       product_value=PRODUCT_VALUE)
        stock -= NUMBER_OF_SALES_PER_MONTH[i]
        restocking = NUMBER_OF_SALES_PER_MONTH[i + 1] if (i < NUMBER_OF_MONTHS - 1) else 0
        stock += restocking

        if annual_net_revenue >= 0 and (annual_net_revenue - monthly_net_revenue) < 0:
            break_even_month = MONTHS[i]

    annual_report(stock=stock,
                  total_purchased=num_units_purchased_year,
                  total_sale=num_units_sold_year,
                  total_cost=annual_cost,
                  gross_revenue=annual_gross_revenue,
                  net_revenue=annual_net_revenue,
                  break_even_month=break_even_month)
