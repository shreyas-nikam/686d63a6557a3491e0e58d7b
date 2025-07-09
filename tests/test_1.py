import pytest
from definition_33ef4dcef47644b18aa957e2e6248489 import calculate_basic_eps

@pytest.mark.parametrize("net_income, preferred_dividends, wa_shares_outstanding, expected", [
    (1000000, 100000, 1000000, 0.9),
    (1000000, 0, 1000000, 1.0),
    (50000, 60000, 100000, 0.0),
    (1000000, 100000, 0, 0.0),
    (1000000, 100000, -100, 0.0)
])
def test_calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding, expected):
    assert calculate_basic_eps(net_income, preferred_dividends, wa_shares_outstanding) == expected
