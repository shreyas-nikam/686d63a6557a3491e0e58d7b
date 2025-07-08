
import pytest
import pandas as pd
import numpy as np
from <your_module> import generate_synthetic_data

def test_generate_synthetic_data_return_type_and_columns():
    """
    Test that generate_synthetic_data returns a pandas Series and contains all expected columns.
    """
    result = generate_synthetic_data(num_records=1)

    assert isinstance(result, pd.Series), "Expected a pandas Series to be returned."

    expected_columns = [
        'Net Income', 'Preferred Dividends', 'Weighted Average Shares Outstanding',
        'Tax Rate', 'Convertible Preferred Stock Count',
        'Convertible Preferred Conversion Ratio', 'Convertible Preferred Dividend Per Share',
        'Convertible Debt Face Value', 'Convertible Debt Coupon Rate',
        'Convertible Debt Conversion Ratio (Shares per $1000)',
        'Stock Option Count', 'Stock Option Exercise Price', 'Average Market Price'
    ]
    assert all(col in result.index for col in expected_columns), "Not all expected columns are present in the generated data."
    assert len(result) == len(expected_columns), "The number of columns in the generated data does not match the expected count."


def test_generate_synthetic_data_data_types_and_non_negativity():
    """
    Test specific data types for key columns and ensure all numeric values are non-negative.
    """
    result = generate_synthetic_data(num_records=1)

    # Check data types for columns specified for explicit int conversion
    assert isinstance(result['Convertible Preferred Stock Count'], (int, np.integer)), "Convertible Preferred Stock Count should be an integer."
    assert isinstance(result['Stock Option Count'], (int, np.integer)), "Stock Option Count should be an integer."
    
    # Check other critical numerical types generated as floats
    # Note: Pandas often stores these as numpy floats.
    assert isinstance(result['Net Income'], (float, np.floating)), "Net Income should be a float."
    assert isinstance(result['Preferred Dividends'], (float, np.floating)), "Preferred Dividends should be a float."
    assert isinstance(result['Weighted Average Shares Outstanding'], (float, np.floating)), "WA Shares Outstanding should be a float."
    assert isinstance(result['Tax Rate'], (float, np.floating)), "Tax Rate should be a float."
    assert isinstance(result['Convertible Preferred Conversion Ratio'], (float, np.floating)), "Convertible Preferred Conversion Ratio should be a float."
    assert isinstance(result['Convertible Preferred Dividend Per Share'], (float, np.floating)), "Convertible Preferred Dividend Per Share should be a float."
    assert isinstance(result['Convertible Debt Face Value'], (float, np.floating)), "Convertible Debt Face Value should be a float."
    assert isinstance(result['Convertible Debt Coupon Rate'], (float, np.floating)), "Convertible Debt Coupon Rate should be a float."
    assert isinstance(result['Convertible Debt Conversion Ratio (Shares per $1000)'], (float, np.floating)), "Convertible Debt Conversion Ratio should be a float."
    assert isinstance(result['Stock Option Exercise Price'], (float, np.floating)), "Stock Option Exercise Price should be a float."
    assert isinstance(result['Average Market Price'], (float, np.floating)), "Average Market Price should be a float."


    # Check that all numeric values are non-negative
    for col in result.index:
        if isinstance(result[col], (int, float, np.integer, np.floating)):
            assert result[col] >= 0, f"Value for '{col}' is negative: {result[col]}"

def test_generate_synthetic_data_edge_case_num_records_zero():
    """
    Test that calling generate_synthetic_data with num_records=0 raises an IndexError,
    as df.iloc[0] would be called on an empty DataFrame.
    """
    with pytest.raises(IndexError, match="single positional indexer is out-of-bounds"):
        generate_synthetic_data(num_records=0)

def test_generate_synthetic_data_preferred_dividends_constraint():
    """
    Test the constraint that Preferred Dividends are adjusted to be <= 10% of Net Income.
    Also verifies it falls within the expected general range after adjustment, considering NI ranges.
    """
    # Run multiple times to increase confidence due to random data generation
    for _ in range(10): # Increased iterations for better coverage of random values
        result = generate_synthetic_data(num_records=1)

        # Constraint: Preferred Dividends <= Net Income * 0.1
        # Use a small tolerance for floating point comparisons
        assert result['Preferred Dividends'] <= result['Net Income'] * 0.1 + 1e-9, \
            f"Preferred Dividends ({result['Preferred Dividends']:.2f}) should be <= 10% of Net Income ({result['Net Income'] * 0.1:.2f})."
        
        # Given Net Income [50M, 500M], NI*0.1 is [5M, 50M]
        # Given initial Preferred Dividends [1M, 10M]
        # Final PD = min(Initial PD, NI*0.1)
        # So, min(1M, 5M) = 1M is the lowest possible.
        # And max(Final PD) is min(10M, any value >=5M) = 10M
        assert result['Preferred Dividends'] >= 1_000_000 - 1e-9, "Preferred Dividends should be at least 1,000,000 after adjustment."
        assert result['Preferred Dividends'] <= 10_000_000 + 1e-9, "Preferred Dividends should be at most 10,000,000 after adjustment."
        assert result['Preferred Dividends'] >= 0, "Preferred Dividends should not be negative."


def test_generate_synthetic_data_market_price_vs_exercise_price_constraint():
    """
    Test the constraint that Average Market Price is generally above
    Stock Option Exercise Price (specifically >= Exercise Price * 1.1).
    """
    # Run multiple times to increase confidence due to random data generation
    for _ in range(10): # Increased iterations for better coverage of random values
        result = generate_synthetic_data(num_records=1)

        # Constraint: Average Market Price >= Stock Option Exercise Price * 1.1
        # Use a small tolerance for floating point comparisons
        assert result['Average Market Price'] >= result['Stock Option Exercise Price'] * 1.1 - 1e-9, \
            f"Average Market Price ({result['Average Market Price']:.2f}) should be >= Stock Option Exercise Price ({result['Stock Option Exercise Price']:.2f}) * 1.1."
        
        # Ensure the base ranges are reasonable for context (values should be positive)
        assert result['Stock Option Exercise Price'] >= 10 - 1e-9, "Stock Option Exercise Price should be at least 10."
        assert result['Average Market Price'] >= 20 - 1e-9, "Average Market Price should be at least 20."
        assert result['Stock Option Exercise Price'] <= 50 + 1e-9, "Stock Option Exercise Price should be at most 50."
        assert result['Average Market Price'] <= 100 + 1e-9, "Average Market Price should be at most 100."
        assert result['Stock Option Exercise Price'] > 0, "Stock Option Exercise Price should be positive."
        assert result['Average Market Price'] > 0, "Average Market Price should be positive."
