from src.load_data_and_prepare_inputs.dimension_names import *


def modify_csps(optimum_parameters, percentage):
    """
    Adjusts the optimum parameters based on the given percentage adjustment and returns the updated parameters.

    Parameters:
        - optimum_parameters (dict): A dictionary containing the original optimum parameters. These should
          include keys like `gamma_weibull_dim` and `mu_weibull_gaussian_dim`, representing specific CSP
          distribution parameters.
        - percentage (float): The percentage adjustment to apply to the parameters. This value can be positive
          (for an increase) or negative (for a decrease). For example, `-0.2` would decrease the parameters by 20%,
          and `0.1` would increase them by 10%.

    Returns:
        - dict: A new dictionary with the same keys as `optimum_parameters`, but with the specified parameters
          (`gamma_weibull_dim`, `mu_weibull_gaussian_dim`) adjusted by the given percentage.
    """
    adjusted_parameters = optimum_parameters.copy()
    percentage_value = 1 + percentage
    adjusted_parameters[gamma_weibull_dim] *= percentage_value
    adjusted_parameters[mu_weibull_gaussian_dim] *= percentage_value
    return adjusted_parameters
