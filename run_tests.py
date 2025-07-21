import pytest
import sys

if __name__ == "__main__":
    # Run all tests in the 'tests' folder and exit with the appropriate status code
    sys.exit(pytest.main(["tests/test_4_model_runs_on_minimal_input_single_country.py::test_model_runs_on_minimal_input"]))
    #sys.exit(pytest.main(["-s","tests"]))