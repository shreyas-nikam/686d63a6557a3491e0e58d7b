import pytest
from definition_d58f47f5544d40bbb4a19e7f9233dd2a import calculate_progress

@pytest.mark.parametrize("costs_incurred, total_expected_costs, expected", [
    # Happy Path - Valid positive numeric inputs
    (0, 100, 0.0),
    (500, 1000, 0.5),
    (1000, 1000, 1.0),
    (420000, 700000, 0.6), # Example from Notebook Specification
    (250.5, 1000.0, 0.2505), # Float inputs
    (1e9, 2e9, 0.5), # Large numbers
    (75, 300, 0.25),
    (1, 3, 1/3), # Resulting in a recurring decimal

    # Edge Cases - total_expected_costs being zero
    (100, 0, ZeroDivisionError),
    (0, 0, ZeroDivisionError),

    # Edge Cases - Negative inputs for costs (mathematically valid but might indicate bad input domain for "progress")
    # Assuming pure division as per stub; function does not validate for positive costs
    (-50, 100, -0.5),
    (50, -100, -0.5),
    (-50, -100, 0.5),

    # Edge Cases - Progress greater than 1.0 (over 100% completion)
    (1200, 1000, 1.2),
    (1500000, 1000000, 1.5),

    # Invalid Input Types - costs_incurred
    ("abc", 100, TypeError),
    ([], 100, TypeError),
    (None, 100, TypeError),
    (True, 100, 0.01), # Booleans treated as numbers (True=1)
    ({'key': 10}, 100, TypeError),
    ((1, 2), 100, TypeError), # Tuple

    # Invalid Input Types - total_expected_costs
    (100, "def", TypeError),
    (100, {}, TypeError),
    (100, None, TypeError),
    (100, False, ZeroDivisionError), # Booleans treated as numbers (False=0)
    (100, [1, 2], TypeError),
    (100, (1, 2), TypeError), # Tuple

    # Invalid Input Types - Both arguments invalid
    ("invalid", "input", TypeError),
    (None, None, TypeError),
    ([], [], TypeError),
    (True, False, ZeroDivisionError), # 1 / 0
])
def test_calculate_progress(costs_incurred, total_expected_costs, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        # If an exception is expected, assert that it is raised
        with pytest.raises(expected):
            calculate_progress(costs_incurred, total_expected_costs)
    else:
        # Otherwise, assert the calculated result
        result = calculate_progress(costs_incurred, total_expected_costs)
        # Use pytest.approx for floating-point comparisons to account for precision issues
        assert result == pytest.approx(expected)