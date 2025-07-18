import pytest
import sys

if __name__ == "__main__":
    # Run all tests in the 'tests' folder and exit with the appropriate status code
    sys.exit(pytest.main(["tests/test_2_5_relative_sales_sums_to_one_per_country_year.py::test_relative_sales_sums_to_one_per_country_year"]))
    #sys.exit(pytest.main(["-s","tests"]))