#API Tests with Pytest

#### Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.


## Getting started

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.


## Running tests

If your tests arec contained inside a folder 'tests', then run the following command : `pytest tests/identifier.py` 

To generate html results, run the following command : `pytest --html=report.html tests/identifier.py`
Test results in `report.html`

The project includes positive and negative tests with and without Pandas (csv reader).
Json requests are based and created on data from csv files.


For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)