import math
import pytest
from kod.area import calculate_rectangle_area
def test_calculate_rectangle_area_with_zero_length_and_width():
    assert calculate_rectangle_area(0, 0) == 0

def test_calculate_rectangle_area_with_length_one_and_width_two():
    assert calculate_rectangle_area(1, 2) == 2

def test_calculate_rectangle_area_with_length_two_point_five_and_width_three_point_one():
    assert calculate_rectangle_area(2.5, 3.1) == 7.75

def test_calculate_rectangle_area_with_negative_length_and_width():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-1, -2)

