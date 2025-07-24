# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

import pytest
import sys


def run_all_tests():
    """
    Main function to execute all unit tests in the 'tests' folder using pytest.

    This function uses pytest to discover and run all test files in the 'tests' directory.
    It passes the '-s' flag to allow real-time output (e.g., print statements) to be visible in the console.

    Optionally, you can uncomment and modify a specific line to run an individual test.

    Steps:
    1. Run pytest on the 'tests' directory with the '-s' option to allow stdout output.
    2. Optionally run a specific test case by modifying the file path and test name.
    3. Exit the script with the same status code returned by pytest.

    Returns:
        None: The script exits with the appropriate status code based on test outcomes.
    """
    # Run all tests in the 'tests' folder with stdout visible
    sys.exit(pytest.main([
        "-s",  # Show print() output
        "--cov=.",  # Measure coverage in current dir
        "--cov-report=term-missing",  # Show missing lines
        "tests"  # Folder with your tests
    ]))

    # To run a specific test only, uncomment the line below and modify the test path as needed:
    # sys.exit(pytest.main(["tests/test_4_model_runs_on_minimal_input_single_country.py::test_model_runs_on_minimal_input"]))


if __name__ == "__main__":
    run_all_tests()
