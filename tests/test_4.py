import pytest
from definition_6a20b8d259c045d69d2ae7dce7a01f6e import calculate_diluted_eps_options

@pytest.mark.parametrize("net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price, expected", [
    (1000000, 100000, 1000000, 100000, 10, 20, 0.94),
    (1000000, 100000, 1000000, 100000, 20, 10, float('inf')),
    (1000000, 100000, 1000000, 0, 10, 20, 0.9),
    (1000000, 100000, 0, 100000, 10, 20, 0.0),
    (1000000, 100000, 1000000, 100000, 10, 10, float('inf'))
])
def test_calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price, expected):
    result = calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price)
    if expected == float('inf'):
        assert result == float('inf')
    else:
        assert abs(result - (expected)) < 0.01
