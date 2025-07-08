
import pytest
from <your_module> import calculate_progress

@pytest.mark.parametrize("costs_incurred, total_expected_costs, expected", [
    # Test case 1: Nominal valid input - fractional progress (from spec Example 8)
    # Expected: 420000 / 700000 = 0.6
    (420000, 700000, 0.6),
    # Test case 2: Edge case - zero costs incurred (project just started)
    # Expected: 0 / 700000 = 0.0
    (0, 700000, 0.0),
    # Test case 3: Edge case - 100% completion (costs incurred equals total expected costs)
    # Expected: 700000 / 700000 = 1.0
    (700000, 700000, 1.0),
    # Test case 4: Edge case - total expected costs is zero (should raise ZeroDivisionError)
    (100, 0, ZeroDivisionError),
    # Test case 5: Edge case - non-numeric inputs (should raise TypeError)
    # The function expects numeric types for division.
    ("abc", 100, TypeError),
])
def test_calculate_progress(costs_incurred, total_expected_costs, expected):
    """
    Tests the calculate_progress function to ensure it correctly calculates progress
    for various scenarios, including valid inputs, edge cases (zero values, 100% completion),
    and error conditions (zero division, incorrect input types).
    """
    try:
        result = calculate_progress(costs_incurred, total_expected_costs)
        # Use pytest.approx for floating-point comparisons to handle precision issues
        assert result == pytest.approx(expected)
    except Exception as e:
        # Assert that the raised exception is of the expected type for error cases
        assert isinstance(e, expected)
