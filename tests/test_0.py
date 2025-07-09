import pytest
import pandas as pd
import numpy as np
from definition_a98ac30c3449430aaad8495106c7a0e0 import generate_synthetic_data

def is_series(obj):
    return isinstance(obj, pd.Series)

def is_number(obj):
    return isinstance(obj, (int, float))

def validate_synthetic_data(synthetic_data):
    assert is_series(synthetic_data)
    assert not synthetic_data.empty
    assert synthetic_data.index.isin([
        'Net Income', 'Preferred Dividends', 'Weighted Average Shares Outstanding',
        'Tax Rate', 'Convertible Preferred Stock Count', 'Convertible Preferred Conversion Ratio',
        'Convertible Preferred Dividend Per Share', 'Convertible Debt Face Value',
        'Convertible Debt Coupon Rate', 'Convertible Debt Conversion Ratio (Shares per $1000)',
        'Stock Option Count', 'Stock Option Exercise Price', 'Average Market Price'
    ]).all()

@pytest.mark.parametrize("num_records", [
    1,
    5,
    10
])
def test_generate_synthetic_data_valid_output(num_records):
    synthetic_data = generate_synthetic_data(num_records)
    validate_synthetic_data(synthetic_data)


def test_generate_synthetic_data_no_records():
    synthetic_data = generate_synthetic_data(0)
    assert is_series(synthetic_data)

def test_generate_synthetic_data_positive_scenarios():
     synthetic_data = generate_synthetic_data(1)
     assert synthetic_data['Net Income'] > 0
     assert synthetic_data['Preferred Dividends'] >= 0
     assert synthetic_data['Weighted Average Shares Outstanding'] > 0
     assert 0 <= synthetic_data['Tax Rate'] <= 1