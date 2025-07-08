import pytest
import pandas as pd
import numpy as np
from definition_1c2c57d0d2e64cc79e9bddb871d1b482 import generate_synthetic_data

# Define the expected columns and their approximate Python data types
# The actual implementation in the notebook specification generates these columns.
EXPECTED_COLUMNS_AND_TYPES = {
    'Net Income': float,
    'Preferred Dividends': float,
    'Weighted Average Shares Outstanding': float,
    'Tax Rate': float,
    'Convertible Preferred Stock Count': int,
    'Convertible Preferred Conversion Ratio': float,
    'Convertible Preferred Dividend Per Share': float,
    'Convertible Debt Face Value': float,
    'Convertible Debt Coupon Rate': float,
    'Convertible Debt Conversion Ratio (Shares per $1000)': float,
    'Stock Option Count': int,
    'Stock Option Exercise Price': float,
    'Average Market Price': float
}

def test_generate_synthetic_data_basic_functionality():
    """
    Tests the basic functionality of generate_synthetic_data with num_records=1.
    Verifies return type, column presence, data types, and value constraints.
    """
    # Use a fixed seed for reproducibility of random data within the test
    np.random.seed(42) 
    
    result_series = generate_synthetic_data(num_records=1)

    # 1. Verify return type
    assert isinstance(result_series, pd.Series), \
        f"Expected pandas.Series, but got {type(result_series)}"

    # 2. Verify all expected columns are present and have correct types
    for col, expected_type in EXPECTED_COLUMNS_AND_TYPES.items():
        assert col in result_series.index, f"Missing expected column: '{col}'"
        assert isinstance(result_series[col], expected_type), \
            f"Column '{col}' has incorrect type. Expected {expected_type.__name__}, got {type(result_series[col]).__name__}"

    # 3. Verify value constraints enforced by the function's internal logic
    # Average Market Price >= Stock Option Exercise Price * 1.1
    # Using a small epsilon for floating point comparison
    assert result_series['Average Market Price'] >= result_series['Stock Option Exercise Price'] * 1.1 - 1e-9, \
        "Average Market Price constraint violated"

    # Preferred Dividends <= Net Income * 0.1
    assert result_series['Preferred Dividends'] <= result_series['Net Income'] * 0.1 + 1e-9, \
        "Preferred Dividends constraint violated"

    # 4. Verify plausible ranges (sanity check, as values are random but within bounds)
    assert 50_000_000 <= result_series['Net Income'] <= 500_000_000
    assert 1_000_000 <= result_series['Preferred Dividends'] <= 10_000_000
    assert 10_000_000 <= result_series['Weighted Average Shares Outstanding'] <= 100_000_000
    assert 0.15 <= result_series['Tax Rate'] <= 0.35
    assert 100_000 <= result_series['Convertible Preferred Stock Count'] <= 1_000_000
    assert 500_000 <= result_series['Stock Option Count'] <= 5_000_000
    
    # All values should be non-negative
    for col in result_series.index:
        assert result_series[col] >= 0, f"Column '{col}' unexpectedly has a negative value: {result_series[col]}"


def test_generate_synthetic_data_returns_single_row_even_if_num_records_greater_than_one():
    """
    Tests that even if num_records is > 1, the function correctly returns only a single Series (row).
    This behavior is specified by the notebook's implementation (df.iloc[0]).
    """
    np.random.seed(43) 
    result_series = generate_synthetic_data(num_records=5) 
    
    assert isinstance(result_series, pd.Series)
    # The length of the Series should correspond to the number of expected columns, indicating a single row.
    assert len(result_series) == len(EXPECTED_COLUMNS_AND_TYPES), \
        f"Expected a single row (Series with {len(EXPECTED_COLUMNS_AND_TYPES)} items), but got {len(result_series)} items."


@pytest.mark.parametrize("num_records_input, expected_exception", [
    (0, IndexError),       # num_records=0 leads to empty DataFrame, then .iloc[0] raises IndexError
    (-5, ValueError),      # Negative num_records causes ValueError in numpy.random functions
    ("invalid", TypeError), # Non-integer string input
    (10.5, TypeError),     # Non-integer float input
    (None, TypeError),     # None input
    ([1], TypeError),      # List input
    ({}, TypeError)        # Dictionary input
])
def test_generate_synthetic_data_invalid_num_records_inputs(num_records_input, expected_exception):
    """
    Tests various invalid inputs for the 'num_records' argument.
    The expected exceptions are based on how numpy.random functions and pandas.DataFrame.iloc[0]
    would behave with such inputs.
    """
    with pytest.raises(expected_exception) as excinfo:
        generate_synthetic_data(num_records_input)
    
    # Optionally, check specific error messages if needed for more robust tests
    # For example, for ValueError from numpy:
    # if expected_exception == ValueError:
    #     assert "size must be non-negative" in str(excinfo.value)
    # For IndexError:
    # if expected_exception == IndexError:
    #     assert "single positional indexer is out-of-bounds" in str(excinfo.value)
