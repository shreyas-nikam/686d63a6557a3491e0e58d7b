import pytest
from definition_0bd80042454044efaf548c0a8f700a2f import update_eps_display

def test_update_eps_display_basic_case(capsys):
    update_eps_display(net_income=1000000, preferred_dividends=100000, wa_shares_outstanding=1000000, tax_rate=0.3,
                       cps_count=0, cps_conv_ratio=0, cps_div_per_share=0,
                       cd_face_value=0, cd_coupon_rate=0, cd_conv_ratio_per_1000=0,
                       so_count=0, so_exercise_price=0, avg_market_price=0)
    captured = capsys.readouterr()
    assert "Basic EPS: $0.90" in captured.out
    assert "Diluted EPS: $0.90" in captured.out

def test_update_eps_display_convertible_preferred(capsys):
    update_eps_display(net_income=1000000, preferred_dividends=100000, wa_shares_outstanding=1000000, tax_rate=0.3,
                       cps_count=100000, cps_conv_ratio=1, cps_div_per_share=1,
                       cd_face_value=0, cd_coupon_rate=0, cd_conv_ratio_per_1000=0,
                       so_count=0, so_exercise_price=0, avg_market_price=0)
    captured = capsys.readouterr()
    assert "Basic EPS: $0.90" in captured.out
    assert "Diluted EPS:" in captured.out

def test_update_eps_display_convertible_debt(capsys):
    update_eps_display(net_income=1000000, preferred_dividends=100000, wa_shares_outstanding=1000000, tax_rate=0.3,
                       cps_count=0, cps_conv_ratio=0, cps_div_per_share=0,
                       cd_face_value=1000000, cd_coupon_rate=0.05, cd_conv_ratio_per_1000=10,
                       so_count=0, so_exercise_price=0, avg_market_price=0)
    captured = capsys.readouterr()
    assert "Basic EPS: $0.90" in captured.out
    assert "Diluted EPS:" in captured.out

def test_update_eps_display_stock_options(capsys):
    update_eps_display(net_income=1000000, preferred_dividends=100000, wa_shares_outstanding=1000000, tax_rate=0.3,
                       cps_count=0, cps_conv_ratio=0, cps_div_per_share=0,
                       cd_face_value=0, cd_coupon_rate=0, cd_conv_ratio_per_1000=0,
                       so_count=100000, so_exercise_price=10, avg_market_price=20)
    captured = capsys.readouterr()
    assert "Basic EPS: $0.90" in captured.out
    assert "Diluted EPS:" in captured.out

def test_update_eps_display_zero_shares(capsys):
    update_eps_display(net_income=1000000, preferred_dividends=100000, wa_shares_outstanding=0, tax_rate=0.3,
                       cps_count=0, cps_conv_ratio=0, cps_div_per_share=0,
                       cd_face_value=0, cd_coupon_rate=0, cd_conv_ratio_per_1000=0,
                       so_count=0, so_exercise_price=0, avg_market_price=0)
    captured = capsys.readouterr()
    assert "Basic EPS: $0.00" in captured.out
    assert "Diluted EPS: $0.00" in captured.out
