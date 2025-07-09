import pytest
from definition_41cf6613812544df8858c11ca535a991 import orchestrate_eps_calculation

def test_orchestrate_eps_calculation_no_dilution():
    """Test case where no dilutive securities exist."""
    ni = 1000000
    pd = 100000
    was = 1000000
    tr = 0.3
    cps_c = 0
    cps_cr = 0
    cps_dps = 0
    cd_fv = 0
    cd_cr = 0
    cd_cr1000 = 0
    so_c = 0
    so_ep = 0
    amp = 0

    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)
    assert basic_eps == (ni - pd) / was
    assert diluted_eps == (ni - pd) / was


def test_orchestrate_eps_calculation_antidilutive_options():
    """Test case where stock options are antidilutive (exercise price > market price)."""
    ni = 1000000
    pd = 100000
    was = 1000000
    tr = 0.3
    cps_c = 0
    cps_cr = 0
    cps_dps = 0
    cd_fv = 0
    cd_cr = 0
    cd_cr1000 = 0
    so_c = 100000
    so_ep = 50
    amp = 20

    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)
    assert basic_eps == (ni - pd) / was
    assert diluted_eps == (ni - pd) / was


def test_orchestrate_eps_calculation_dilutive_convertible_preferred():
    """Test case with dilutive convertible preferred stock."""
    ni = 1000000
    pd = 100000
    was = 1000000
    tr = 0.3
    cps_c = 100000
    cps_cr = 2
    cps_dps = 1
    cd_fv = 0
    cd_cr = 0
    cd_cr1000 = 0
    so_c = 0
    so_ep = 0
    amp = 0

    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)
    
    expected_diluted_eps = ni / (was + cps_c * cps_cr)
    
    assert basic_eps == (ni - pd) / was
    assert diluted_eps <= basic_eps

def test_orchestrate_eps_calculation_dilutive_convertible_debt():
    """Test case with dilutive convertible debt."""
    ni = 1000000
    pd = 100000
    was = 1000000
    tr = 0.3
    cps_c = 0
    cps_cr = 0
    cps_dps = 0
    cd_fv = 500000
    cd_cr = 0.05
    cd_cr1000 = 20
    so_c = 0
    so_ep = 0
    amp = 0
    interest_expense = cd_fv * cd_cr
    after_tax_interest_savings = interest_expense * (1 - tr)

    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)
    
    expected_diluted_eps = (ni + after_tax_interest_savings - pd) / (was + (cd_fv / 1000) * cd_cr1000)

    assert basic_eps == (ni - pd) / was
    assert diluted_eps <= basic_eps

def test_orchestrate_eps_calculation_dilutive_options():
    """Test case with dilutive stock options."""
    ni = 1000000
    pd = 100000
    was = 1000000
    tr = 0.3
    cps_c = 0
    cps_cr = 0
    cps_dps = 0
    cd_fv = 0
    cd_cr = 0
    cd_cr1000 = 0
    so_c = 100000
    so_ep = 20
    amp = 50
    
    proceeds_from_exercise = so_c * so_ep
    shares_repurchased = proceeds_from_exercise / amp
    incremental_shares = so_c - shares_repurchased

    basic_eps, diluted_eps = orchestrate_eps_calculation(ni, pd, was, tr, cps_c, cps_cr, cps_dps, cd_fv, cd_cr, cd_cr1000, so_c, so_ep, amp)

    expected_diluted_eps = (ni - pd) / (was + incremental_shares)

    assert basic_eps == (ni - pd) / was
    assert diluted_eps <= basic_eps
