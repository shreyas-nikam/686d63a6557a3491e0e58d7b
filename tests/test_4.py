import pytest
from definition_7740ff4b4b1343c183367acb0febc0fe import calculate_diluted_eps_options

@pytest.mark.parametrize(
    "net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price, expected_output",
    [
        # Test Case 1: Standard Dilutive Scenario (Exercise Price < Average Market Price)
        # Expected: Numerator (100k-10k) = 90k. Proceeds = 1k*20=20k. Shares Repurchased = 20k/30 = 666.666...
        # Incremental Shares = 1k - 666.666... = 333.333... Denominator = 10k + 333.333... = 10333.333...
        # EPS = 90k / 10333.333... = 8.709677419354838
        (100_000, 10_000, 10_000, 1_000, 20, 30, 8.709677419354838),

        # Test Case 2: Antidilutive Scenario (Exercise Price == Average Market Price)
        # As per the logic and docstring, if so_exercise_price >= avg_market_price, it's antidilutive.
        (100_000, 10_000, 10_000, 1_000, 25, 25, float('inf')),

        # Test Case 3: Antidilutive Scenario (Exercise Price > Average Market Price)
        # Also triggers the antidilution rule.
        (100_000, 10_000, 10_000, 1_000, 30, 25, float('inf')),
        
        # Test Case 4: No Stock Options Outstanding (so_count = 0)
        # Incremental shares should be 0, leading to Basic EPS calculation (if no other factors)
        # Expected: Numerator (100k-10k) = 90k. Denominator = 10k + 0 = 10k. EPS = 90k/10k = 9.0
        (100_000, 10_000, 10_000, 0, 20, 30, 9.0),

        # Test Case 5: Negative Net Income available to common shareholders
        # Numerator (5k-10k) = -5k. Denominator (10k + 333.333...) = 10333.333...
        # Expected: -5k / 10333.333... = -0.4838709677419355
        (5_000, 10_000, 10_000, 1_000, 20, 30, -0.4838709677419355),
    ]
)
def test_calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price, expected_output):
    result = calculate_diluted_eps_options(net_income, preferred_dividends_total, wa_shares_outstanding, so_count, so_exercise_price, avg_market_price)
    
    # Special handling for float('inf') comparison
    if expected_output == float('inf'):
        assert result == float('inf')
    else:
        # Use pytest.approx for floating point comparisons to account for precision differences
        assert result == pytest.approx(expected_output)
