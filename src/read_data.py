import os

import pandas as pd
from pandas import DataFrame

path_to_csv_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
path_to_xlsx_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_data_from_csv(path_to_file: str) -> DataFrame:
    csv_data = pd.read_csv(path_to_file, delimiter=";")
    return csv_data


def get_data_from_xlsx(path_to_file: str) -> DataFrame:
    excel_data = pd.read_excel(path_to_file)
    return excel_data


print(get_data_from_csv(path_to_csv_file))
print(get_data_from_xlsx(path_to_xlsx_file))
