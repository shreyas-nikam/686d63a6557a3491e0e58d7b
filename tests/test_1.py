import pytest
from definition_eb84bf9b62f6428dadc27694325eef3a import calculate_basic_eps

@pytest.mark.parametrize("net_income, preferred_dividends, wa_shares_outstanding, expected", [
    # Test case 1: Standard calculation with positive values
    (100000, 10000, 10000, 9.0),
    # Test case 2: Preferred dividends exceed net income (effective net income becomes 0)
    (50000, 60000, 10000, 0.0),
    # Test case 3: Zero weighted average shares outstanding (should return 0.0 to avoid ZeroDivisionError)
    (100000, 10000, 0, 0.0),
    # Test case 4: Negative weighted average shares outstanding (should return 0.0)
    (100000, 10000, -500, 0.0),
    # Test case 5: Invalid input type (string for net_income), expecting TypeError
    ("abc", 10000, 10000, TypeError),
])
def test_calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding)
    else:
        result = calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding)
        assert result == pytest.approx(expected)