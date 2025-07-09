import pytest
from definition_a8542a3504e84aa5af0817121c5a8fa7 import orchestrate_eps_calculation

@pytest.mark.parametrize(
    "name, net_income, preferred_dividends, wa_shares_outstanding, tax_rate, "
    "cps_count, cps_conv_ratio, cps_div_per_share, "
    "cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000, "
    "so_count, so_exercise_price, avg_market_price, "
    "expected_basic_eps, expected_diluted_eps",
    [
        # Test Case 1: Basic EPS - No dilutive securities (all zero for dilutive params)
        ("Basic_EPS_Standard", 1000, 100, 100, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9.0, 9.0),
        
        # Test Case 2: Only Convertible Preferred Stock (CPS) is dilutive
        # Basic EPS: (1000-100)/100 = 9.0
        # CPS dilution: Net income becomes 1000 (PD added back), Shares = 100 + (10*5) = 150. Diluted EPS = 1000/150 = 6.666...
        ("CPS_Dilutive", 1000, 100, 100, 0.25, 10, 5, 10, 0, 0, 0, 0, 0, 0, 9.0, 6.666666666666667),

        # Test Case 3: Only Convertible Debt (CD) is dilutive
        # Basic EPS: (100-0)/10 = 10.0
        # CD dilution: After-tax interest savings = 1000*0.01*(1-0.2) = 8. New shares = (1000/1000)*10 = 10.
        # Diluted EPS = (100+8)/(10+10) = 108/20 = 5.4.
        ("CD_Dilutive", 100, 0, 10, 0.2, 0, 0, 0, 1000, 0.01, 10, 0, 0, 0, 10.0, 5.4),

        # Test Case 4: Only Stock Options (SO) are dilutive
        # Basic EPS: (100-0)/10 = 10.0
        # SO dilution: Proceeds = 10*5=50. Shares repurchased = 50/10=5. Incremental shares = 10-5=5.
        # Diluted EPS = (100-0)/(10+5) = 100/15 = 6.666...
        ("SO_Dilutive", 100, 0, 10, 0.25, 0, 0, 0, 0, 0, 0, 10, 5, 10, 10.0, 6.666666666666667),

        # Test Case 5: Complex Scenario - All three securities are dilutive
        # Basic EPS: (1000-100)/100 = 9.0
        # CPS Dilutive: Num +100 (PD addback), Denom +50 (shares)
        # CD Dilutive: Num +8 (after-tax interest), Denom +10 (shares)
        # SO Dilutive: Denom +10 (incremental shares)
        # Final Num = (1000-100) + 100 (from CPS) + 8 (from CD) = 1008
        # Final Denom = 100 + 50 (from CPS) + 10 (from CD) + 10 (from SO) = 170
        # Diluted EPS = 1008/170 = 5.929411764705882
        ("Complex_All_Dilutive", 1000, 100, 100, 0.2, # Core financial inputs
         10, 5, 10,                                  # Convertible Preferred Stock (dilutive)
         1000, 0.01, 10,                             # Convertible Debt (dilutive)
         20, 10, 20,                                 # Stock Options (dilutive)
         9.0, 5.929411764705882),
    ]
)
def test_eps_calculations(name, net_income, preferred_dividends, wa_shares_outstanding, tax_rate,
                          cps_count, cps_conv_ratio, cps_div_per_share,
                          cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000,
                          so_count, so_exercise_price, avg_market_price,
                          expected_basic_eps, expected_diluted_eps):
    """
    Tests the orchestrate_eps_calculation function for various scenarios,
    including basic EPS, individual dilutive securities, and a complex mix.
    """
    basic_eps, diluted_eps = orchestrate_eps_calculation(
        net_income, preferred_dividends, wa_shares_outstanding, tax_rate,
        cps_count, cps_conv_ratio, cps_div_per_share,
        cd_face_value, cd_coupon_rate, cd_conv_ratio_per_1000,
        so_count, so_exercise_price, avg_market_price
    )

    assert pytest.approx(basic_eps) == expected_basic_eps, f"Test '{name}': Basic EPS mismatch."
    assert pytest.approx(diluted_eps) == expected_diluted_eps, f"Test '{name}': Diluted EPS mismatch."