import pytest
from definition_c5ace69b941f42a6887746541514bde6 import orchestrate_eps_calculation

@pytest.mark.parametrize(
    "ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp, expected_basic_eps, expected_diluted_eps",
    [
        # Test Case 1: No dilutive securities - Basic EPS equals Diluted EPS
        (100_000, 10_000, 10_000, 0.2, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 9.0, 9.0),

        # Test Case 2: All three types of securities are dilutive
        # Basic EPS: (1,000,000 - 100,000) / 100,000 = 9.0
        # CPS Dilution: 10,000 * 5 = 50,000 shares; Income: 100,000 (PD added back)
        # CD Dilution: (1,000,000/1000)*20 = 20,000 shares; Income: 1,000,000*0.05*(1-0.25) = 37,500
        # SO Dilution: 20,000 - (20,000*40/50) = 20,000 - 16,000 = 4,000 shares; Income: 0
        # Total Diluted Shares: 100,000 + 50,000 + 20,000 + 4,000 = 174,000
        # Total Diluted Income: (1,000,000 - 100,000) + 100,000 (from CPS) + 37,500 (from CD) + 0 (from SO) = 1,037,500
        # Diluted EPS: 1,037,500 / 174,000 = 5.962643678160919
        (1_000_000, 100_000, 100_000, 0.25, 10_000, 5.0, 10.0, 1_000_000, 0.05, 20.0, 20_000, 40.0, 50.0, 9.0, pytest.approx(5.962643678160919)),

        # Test Case 3: Stock Options are Anti-dilutive (and other securities are zero)
        # Basic EPS: (100,000 - 10,000) / 10,000 = 9.0
        # SO: Exercise Price (50) >= Avg Market Price (40), so options are anti-dilutive.
        # Diluted EPS should equal Basic EPS.
        (100_000, 10_000, 10_000, 0.25, 0, 0.0, 0.0, 0, 0.0, 0.0, 10_000, 50.0, 40.0, 9.0, 9.0),

        # Test Case 4: Edge Case - Zero Weighted Average Shares Outstanding
        # Basic EPS and Diluted EPS should both be 0.0 due to division by zero handling.
        (100_000, 10_000, 0, 0.25, 10_000, 5.0, 10.0, 1_000_000, 0.05, 20.0, 20_000, 40.0, 50.0, 0.0, 0.0),

        # Test Case 5: Mixed Dilution/Antidilution with Capping
        # Basic EPS: (1,000,000 - 100,000) / 100,000 = 9.0
        # CPS: Dilutive (as per TC2 contribution)
        # CD: Dilutive (as per TC2 contribution)
        # SO: Anti-dilutive (Exercise Price 60 > Avg Market Price 50)
        # Expected Diluted EPS will be from CPS + CD, SO excluded.
        # Total Diluted Shares (CPS+CD only): 100,000 + 50,000 + 20,000 = 170,000
        # Total Diluted Income (CPS+CD only): (1,000,000 - 100,000) + 100,000 + 37,500 = 1,037,500
        # Diluted EPS (calculated): 1,037,500 / 170,000 = 6.102941176470588
        (1_000_000, 100_000, 100_000, 0.25, 10_000, 5.0, 10.0, 1_000_000, 0.05, 20.0, 20_000, 60.0, 50.0, 9.0, pytest.approx(6.102941176470588)),
    ]
)
def test_orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp, expected_basic_eps, expected_diluted_eps):
    basic_eps, diluted_eps = orchestrate_eps_calculation(
        ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp
    )

    assert basic_eps == expected_basic_eps
    assert diluted_eps == expected_diluted_eps