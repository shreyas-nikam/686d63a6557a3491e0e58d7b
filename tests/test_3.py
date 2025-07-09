import pytest
from definition_eee129cbc6ba41e4937defbeb3c66dbb import calculate_diluted_eps_debt

@pytest.mark.parametrize("net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate, expected", [
    (1000000, 100000, 1000000, 1000000, 0.05, 20, 0.3, 965686/1020000),
    (1000000, 100000, 1000000, 0, 0.05, 20, 0.3, 900000/1000000),
    (1000000, 100000, 1000000, 1000000, 0, 20, 0.3, 900000/1020000),
    (1000000, 100000, 0, 1000000, 0.05, 20, 0.3, 1000000 * (1 + 0.05 * (1 - 0.3)) / (1000000/1000 * 20)),
    (1000000, 100000, 1000000, 1000000, 0.05, 0, 0.3, 965686/1000000),
])
def test_calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate, expected):
    assert abs(calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate) - expected) < 1e-6
