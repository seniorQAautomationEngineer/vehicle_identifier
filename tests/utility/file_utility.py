import csv
import pandas as pd
import numpy as np


def read_from_csv(filename):
    test_data = []
    with open(filename, newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)
        for row in data:
            test_data.append(row)
    return test_data


def read_from_csv_pandas(filename):
    df = pd.read_csv(filename, sep=',', engine='python')
    print(df)
    return df


def create_one_item_convert(length, width, height, weight, quantity):
    item_obj = {"length": float(length), "width": float(width), "height": float(height), "weight": float(weight), "quantity": float(quantity)}
    return item_obj


def create_one_item(length, width, height, weight, quantity):
    item_obj = {"length": length, "width": width, "height": height, "weight": weight, "quantity": quantity}
    return item_obj


def randomDigits(start, end):
    return np.random.uniform(start, end)
