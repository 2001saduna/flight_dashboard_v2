import pytest
import parser_1
from unittest.mock import patch
from csv_distance_calculation import calculate_distance

@pytest.fixture()
def result_fixture():
    """Fixture to read the file"""
    result = parser_1.readTextFile('test.txt')
    yield result

def test_get_coordinates(result_fixture):
    y = calculate_distance(result_fixture)
    expected_results = 2.0
    assert expected_results == y




