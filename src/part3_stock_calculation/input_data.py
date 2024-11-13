from src.part1_transportation_model.input_data import eu_countries_and_norway
eu_9 = ['Austria', 'Denmark', 'Finland', 'France', 'Germany', 'Ireland', 'Italy', 'Netherlands', 'Spain']
eu_26_and_norway = eu_countries_and_norway.copy()
eu_26_and_norway.remove('Bulgaria')

eu_country_groups = {
    'EU-9': eu_9,
    'EU-26+Norway': eu_26_and_norway,
    'EU-27+Norway': eu_countries_and_norway # Assuming this is the full set
}

stock_years = [2014, 2050]
historical_csp ='No'