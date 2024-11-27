from src.part1_transportation_model.input_data import eu_countries_and_norway
from src.load_data_and_prepare_inputs.dimension_names import eu_9_label, eu_26_plus_norway_label, \
    eu_27_plus_norway_label


eu_9 = ['Austria', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Netherlands', 'Spain']
eu_26_and_norway = eu_countries_and_norway.copy()
eu_26_and_norway.remove('Bulgaria')

eu_country_groups = {
    eu_9_label: eu_9,
    eu_26_plus_norway_label: eu_26_and_norway,
    eu_27_plus_norway_label: eu_countries_and_norway # Assuming this is the full set
}

stock_years = [2014, 2050]
csp_data_ref_year = 2021
csp_available_years = 45
historical_csp ='No'

save_options_stock = {
    "stock_data_filename": "3_1_stock_data_including_vehicle_age.csv",
    "stock_shares_filename": "3_2_stock_shares.csv"
}