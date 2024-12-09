def get_country_group_names(country_names, group_number, number_of_countries_group):
    """
    Returns a subset of country names based on the specified group number.

    Args:
        country_names (list): A list of all country names.
        group_number (int): The group number to select. Valid values are `1` (first group) or `2` (second group).
        number_of_countries_group (int): The number of countries per group.

    Returns:
    - list: List of country names for the specified group.
    """
    if group_number == 1:
        return country_names[:number_of_countries_group]
    else:
        return country_names[number_of_countries_group:]
