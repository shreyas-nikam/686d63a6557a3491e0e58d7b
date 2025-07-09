import pytest
from definition_44a2866f8f1e4aeea8563eaf74a4b4b6 import calculate_diluted_eps_debt

@pytest.mark.parametrize(
    "net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate, expected_eps",
    [
        # Test Case 1: Basic Dilutive Scenario
        # Standard positive values, should result in a diluted EPS.
        # Numerator: 10M + (10M * 0.05 * (1-0.25)) - 0 = 10M + 375K = 10,375,000
        # Denominator: 5M + (10M / 1000 * 20) = 5M + 200K = 5,200,000
        # EPS = 10,375,000 / 5,200,000 = 1.9951923076923077
        (10_000_000, 0, 5_000_000, 10_000_000, 0.05, 20, 0.25, 1.9951923076923077),

        # Test Case 2: Zero Convertible Debt Impact
        # If cd_face_value is 0, interest savings and new shares from CD are 0.
        # The calculation should effectively be (net_income - preferred_dividends_total) / wa_shares_outstanding.
        # Numerator: 10M + 0 - 1M = 9,000,000
        # Denominator: 5M + 0 = 5,000,000
        # EPS = 9,000,000 / 5,000,000 = 1.8
        (10_000_000, 1_000_000, 5_000_000, 0, 0.05, 20, 0.25, 1.8),

        # Test Case 3: Denominator is Zero (Edge Case)
        # If weighted average shares outstanding + new shares from conversion is zero or less, the function should return 0.0
        # as per the notebook's internal logic for division by zero / non-positive shares.
        # Here, wa_shares_outstanding=0 and cd_conv_ratio_per_1000=0 (no new shares).
        # Denominator: 0 + (10M / 1000 * 0) = 0
        (10_000_000, 0, 0, 10_000_000, 0.05, 0, 0.25, 0.0),

        # Test Case 4: Negative Net Income (Loss Scenario)
        # EPS can be negative if the company has a net loss.
        # Numerator: -5M + 0 - 0 = -5,000,000
        # Denominator: 10M + 0 = 10,000,000
        # EPS = -5,000,000 / 10,000,000 = -0.5
        (-5_000_000, 0, 10_000_000, 0, 0, 0, 0.25, -0.5),

        # Test Case 5: Debt that results in an "Antidilutive" calculated EPS by this function.
        # This function calculates the potential EPS if converted. Antidilution check (compared to Basic EPS)
        # happens in the orchestrator. This function should return the calculated value, even if higher than Basic EPS.
        # Numerator: 10M + (1M * 0.1 * (1-0.2)) - 0 = 10M + 80K = 10,080,000
        # Denominator: 10M + (1M / 1000 * 1) = 10M + 1K = 10,001,000
        # EPS = 10,080,000 / 10,001,000 = 1.0078992100789921
        (10_000_000, 0, 10_000_000, 1_000_000, 0.1, 1, 0.2, 1.0078992100789921),
    ]
)
def test_calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate, expected_eps):
    result = calculate_diluted_eps_debt(net_income, preferred_dividends_total, wa_shares_outstanding, cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, tax_rate)
    assert result == pytest.approx(expected_eps)