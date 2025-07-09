import pytest
import pandas as pd
import numpy as np
from definition_13ae987abd424541bd955a9d73d83ffe import generate_synthetic_data

@pytest.mark.parametrize("num_records, expected_type, expected_error, check_constraints", [
    (1, pd.Series, None, True),  # Test Case 1: Standard positive integer (single record output)
    (0, None, IndexError, False), # Test Case 2: Edge case for 0 records, expects IndexError as .iloc[0] on empty DF
    (5, pd.Series, None, True),   # Test Case 3: Positive integer > 1 (function generates multiple, but returns only 1st)
    ("invalid", None, TypeError, False), # Test Case 4: Invalid type for num_records (string), expects TypeError from numpy
    (-1, None, ValueError, False), # Test Case 5: Negative integer for num_records, expects ValueError from numpy
])
def test_generate_synthetic_data(num_records, expected_type, expected_error, check_constraints):
    if expected_error:
        with pytest.raises(expected_error):
            generate_synthetic_data(num_records)
    else:
        result = generate_synthetic_data(num_records)
        
        # 1. Verify the return type is a pandas Series
        assert isinstance(result, expected_type)
        
        # 2. Verify all expected columns are present and count is correct
        expected_columns = [
            'Net Income', 'Preferred Dividends', 'Weighted Average Shares Outstanding',
            'Tax Rate', 'Convertible Preferred Stock Count', 'Convertible Preferred Conversion Ratio',
            'Convertible Preferred Dividend Per Share', 'Convertible Debt Face Value',
            'Convertible Debt Coupon Rate', 'Convertible Debt Conversion Ratio (Shares per $1000)',
            'Stock Option Count', 'Stock Option Exercise Price', 'Average Market Price'
        ]
        assert len(result) == len(expected_columns)
        assert all(col in result.index for col in expected_columns)

        if check_constraints:
            # 3. Verify specific columns are of integer type
            assert isinstance(result['Convertible Preferred Stock Count'], (int, np.integer))
            assert isinstance(result['Stock Option Count'], (int, np.integer))

            # 4. Verify the custom logic constraints applied by the function
            # 'Average Market Price' should be generally above 'Stock Option Exercise Price' * 1.1
            assert result['Average Market Price'] >= result['Stock Option Exercise Price'] * 1.1 - 1e-9 

            # 'Preferred Dividends' should be less than or equal to 'Net Income' * 0.1
            assert result['Preferred Dividends'] <= result['Net Income'] * 0.1 + 1e-9

            # 5. Verify all generated numerical values are non-negative
            for col in expected_columns:
                assert result[col] >= 0
