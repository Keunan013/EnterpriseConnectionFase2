from app.operation.fill_out_report import fill_out_reports
from app.util.color import Color

NUM_OF_ASTERISKS = 225


def print_reports() -> None:
    print(f'{Color.OK_GREEN}*{Color.RESET}' * NUM_OF_ASTERISKS + '\n')
    fill_out_reports()
    print(f'{Color.OK_GREEN}*{Color.RESET}' * NUM_OF_ASTERISKS)
