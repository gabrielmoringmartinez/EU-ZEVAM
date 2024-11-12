from src.part2_survival_rates.csp_parameters_optimization_algorithms import run_diff_evol_algorithm_weibull, \
    run_diff_evol_algorithm_weibull_gaussian
from src.part2_survival_rates.select_optimal_type_of_distribution import select_optimal_type_of_distribution


def calculate_csp_parameters(survival_rates, year):
    """
        Calculates optimal CSP parameters for country-specific Weibull and Weibull-Gaussian survival curves. Bounds
        selected for the optimization based on the conclusion extracted in Held, 2021 and described in Appendix F

        Parameters:
            survival_rates (DataFrame): Contains 'country label' and 'survival rate' columns.
            year (int): The year of the data of empirical survival rates.

        Returns:
            tuple:
                - DataFrame: Optimized CSP parameters per country, including the best-fit parameters and distribution
                  type.
                - dict: A dictionary where keys are distribution types ('Weibull' or 'WG'), and values are lists of
                  countries.
        """
    bounds_weibull = [(5, 40), (2, 6)]
    k = [2, 100]
    mu = [5, 30]
    sigma = [5, 30]
    bounds_gaussian = [k, mu, sigma]
    country_names = survival_rates['geo country'].unique()
    optimum_parameters_weibull = run_diff_evol_algorithm_weibull(bounds_weibull, country_names, survival_rates)
    optimum_parameters_weibull_gaussian = run_diff_evol_algorithm_weibull_gaussian(bounds_gaussian, country_names,
                                                                                   survival_rates,
                                                                                   optimum_parameters_weibull)
    optimum_parameters_weibull_gaussian = select_optimal_type_of_distribution(optimum_parameters_weibull_gaussian)
    optimum_parameters_weibull_gaussian.to_csv(f'outputs/2_1_optimum_parameters_csp_curves.csv', sep=';', index=False,
                                               decimal=',')
    country_opt_dist_dict = {dist: optimum_parameters_weibull_gaussian.loc[optimum_parameters_weibull_gaussian['distribution'] == dist, 'geo country'].tolist()
                             for dist in optimum_parameters_weibull_gaussian['distribution'].unique()}
    return optimum_parameters_weibull_gaussian, country_opt_dist_dict
