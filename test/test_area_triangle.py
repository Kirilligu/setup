import math
import pytest
from kod.radius import area_triangle
def test_calculate_triangle_area_with_valid_side_lengths():
    assert calculate_triangle_area(3, 4, 5) == 6.0

def test_calculate_triangle_area_with_invalid_side_lengths():
    with pytest.raises(ValueError):
        calculate_triangle_area(-1, 2, 3)

def test_calculate_triangle_area_with_zero_side_lengths():
    assert calculate_triangle_area(0, 0, 0) == 0.0

def test_calculate_triangle_area_with_floating_point_side_lengths():
    assert math.isclose(calculate_triangle_area(3.5, 4.2, 5.1), 7.890312193832433)

