# distribution_bounds defines the parameter bounds for fitting Weibull and Gaussian distributions

distribution_bounds = {
    'weibull': [(5, 40),  # Bounds for Weibull average lifetime (gamma): [min, max]
                (2, 6)],  # Bounds for Weibull shape parameter (beta): [min, max]
    'gaussian': {
        'k': [2, 100],    # Bounds for Gaussian stretch (k): [min, max]
        'mu': [5, 30],    # Bounds for Gaussian mean (mu): [min, max]
        'sigma': [5, 30]  # Bounds for Gaussian standard deviation (sigma): [min, max]
    }
}