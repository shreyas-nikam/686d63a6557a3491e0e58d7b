import pytest
from definition_a06f2bb09a55475b82d7a1850e9645c9 import calculate_diluted_eps_preferred

@pytest.mark.parametrize("net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio, expected", [
    (1000000, 100000, 100000, 10000, 10, 0.8333333333333334),
    (1000000, 100000, 100000, 0, 10, 9.0),
    (1000000, 100000, 100000, 10000, 0, 9.0),
    (1000000, 100000, 100000, 10000, 10, 0.8333333333333334),
    (1000000, 100000, 0, 10000, 10, 100.0)
])
def test_calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio, expected):
    assert calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio) == expected
