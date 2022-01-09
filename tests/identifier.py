import pytest as pytest
import requests
import json
import jsonpath
from utility.file_utility import *
from utility.numpyencoder import NumpyEncoder

baseUrl = "https://url.com"
vehicle_size_endpoint = "/vehicle_size"
data_file = "tests/data/input_vehicles.csv"
negative_data_file = "tests/data/input_vehicles_negative.csv"
requirements_file = "tests/data/requirements.csv"


# 1.  Positive tests with Pandas
def test_size_of_vehicles_pandas():
    jsArray = []
    df = pd.read_csv(data_file)
    for i in df.index:
        jsArray.insert(i, create_one_item(df.loc[df.index[i], "length"], df.loc[df.index[i], "width"],
                                          df.loc[df.index[i], "height"], df.loc[df.index[i], "weight"],
                                          df.loc[df.index[i], "quantity"]))
    inputData = json.dumps(jsArray, indent=4, sort_keys=True, separators=(', ', ': '), ensure_ascii=False,
                           cls=NumpyEncoder)
    print(inputData)
    response = requests.post(url=baseUrl + vehicle_size_endpoint, json=inputData)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    actual_vehicle_size = jsonpath.jsonpath(responseJson, '$.calculated_vehicle_size')
    assert actual_vehicle_size is not None


# 1.  Positive tests without Pandas
def test_size_of_vehicles_positive():
    jsArray = []
    index_object = 0
    with open(data_file, newline="") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile, delimiter=',')
        for row in csv_dict_reader:
            index_object += 1
            jsArray.insert(index_object,
                           create_one_item_convert(row['length'], row['width'], row['height'], row['weight'],
                                                   row['quantity']))
    inputData = json.dumps(jsArray, sort_keys=True, indent=3)
    print(inputData)
    response = requests.post(url=baseUrl + vehicle_size_endpoint, json=inputData)
    responseJson = json.loads(response.text)
    print(responseJson)
    assert response.status_code == 200
    actual_vehicle_size = jsonpath.jsonpath(responseJson, '$.calculated_vehicle_size')
    assert actual_vehicle_size is not None


# Negative tests
# 1. Zero input length
# 2. Zero input width
# 3. Zero input height
# 4. Zero input weight
# 5. Zero input quantity
# 6. Zero input all values
# 7. Letters input length
# 8. Letters input width
# 9. Letters input height
# 10. Letters input weight
# 11. Letters input quantity
# 12. Spec character input length
# 13. Spec character width
# 14. Spec character height
# 15. Spec character weight
# 16. Spec character quantity
# 17.  -1 in all values.


@pytest.mark.parametrize("index,length,width,height,weight,quantity", read_from_csv(negative_data_file))
def test_size_of_vehicles_spec_negative(index, length, width, height, weight, quantity):
    jsArray = []
    index_obj = int(index)
    jsArray.insert(index_obj, create_one_item(length, width, height, weight, quantity))
    inputData = json.dumps(jsArray, sort_keys=True, indent=3)
    print(inputData)
    response = requests.post(url=baseUrl + vehicle_size_endpoint, json=inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 400
    print(responseJson)


# Generate random values.
def test_size_of_vehicles_negative_random():
    jsArray = []
    index_object = 3
    length = randomDigits(5, 100)
    width = randomDigits(2, 10)
    height = randomDigits(4, 1000)
    weight = randomDigits(1, 1000)
    quantity = randomDigits(1, 100)
    jsArray.insert(index_object, create_one_item(length, width, height, weight, quantity))
    inputData = json.dumps(jsArray, sort_keys=True, indent=3)
    print(inputData)
    response = requests.post(url=baseUrl + vehicle_size_endpoint, json=inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 400
    print(responseJson)
