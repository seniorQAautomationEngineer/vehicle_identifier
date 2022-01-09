import pandas as pd
from tests.utility.file_utility import read_from_csv_pandas

requirements_file = "../data/requirements.csv"

# Draft for parsing data from requirements


def parse_data_from_requirements():
    requirements = read_from_csv_pandas(requirements_file)
    df = pd.DataFrame(requirements)
    sedan_max_length = df.loc[df.vehicle_type == 'sedan', 'max_length']
    sedan_max_height = df.loc[df.vehicle_type == 'sedan', 'max_height']
    sedan_max_width = df.loc[df.vehicle_type == 'sedan', 'max_width']
    sedan_max_single_weight = df.loc[df.vehicle_type == 'sedan', 'max_single_weight']
    sedan_max_total_weight = df.loc[df.vehicle_type == 'sedan', 'max_total_weight']


parse_data_from_requirements()