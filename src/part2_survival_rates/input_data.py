# distribution_bounds defines the parameter bounds for fitting Weibull and Gaussian distributions
from src.load_data_and_prepare_inputs.dimension_names import *

distribution_bounds = {
    weibull_label: [(5, 40),  # Bounds for Weibull average lifetime (gamma): [min, max]
                    (2, 6)],  # Bounds for Weibull shape parameter (beta): [min, max]
    weibull_gaussian_label: {
        k_weibull_gaussian_dim: [2, 100],    # Bounds for Gaussian stretch (k): [min, max]
        mu_weibull_gaussian_dim: [5, 30],    # Bounds for Gaussian mean (mu): [min, max]
        sigma_weibull_gaussian_dim: [5, 30]  # Bounds for Gaussian standard deviation (sigma): [min, max]
    }
}
