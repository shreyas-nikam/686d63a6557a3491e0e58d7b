import pytest
from definition_4d67ada6ed254d5e91f8273663c20fb2 import calculate_diluted_eps_preferred

@pytest.mark.parametrize(
    "net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio, expected",
    [
        # Test Case 1: Standard dilutive scenario
        (1_000_000, 100_000, 1_000_000, 100_000, 2.0, 1_000_000 / (1_000_000 + 100_000 * 2.0)),
        # Test Case 2: No convertible preferred stock (cps_count = 0)
        (500_000, 50_000, 1_000_000, 0, 2.0, 500_000 / (1_000_000 + 0 * 2.0)),
        # Test Case 3: Denominator becomes zero or negative (wa_shares_outstanding + new_shares_from_cps <= 0)
        # In this specific implementation, if wa_shares_outstanding is 0 and cps_count is 0, denominator is 0.
        (1_000_000, 100_000, 0, 0, 0, 0.0),
        # Test Case 4: Negative net income (loss)
        (-500_000, 0, 1_000_000, 100_000, 1.0, -500_000 / (1_000_000 + 100_000 * 1.0)),
        # Test Case 5: Large numbers for realistic scenario
        (500_000_000, 10_000_000, 100_000_000, 5_000_000, 3.0, 500_000_000 / (100_000_000 + 5_000_000 * 3.0)),
    ]
)
def test_calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio, expected):
    """
    Tests the calculate_diluted_eps_preferred function covering various scenarios
    including standard dilution, no convertible preferred stock, zero denominator,
    negative net income, and large numbers.
    """
    result = calculate_diluted_eps_preferred(net_income, preferred_dividends_total, wa_shares_outstanding, cps_count, cps_conv_ratio)
    assert result == pytest.approx(expected)