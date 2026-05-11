"""Split country lists into plotting groups."""

# SPDX-FileCopyrightText: 2025 German Aerospace Center, Gabriel Möring-Martínez
# SPDX-License-Identifier: MIT

def get_country_group_names(country_names, group_number, number_of_countries_group):
    """
    Return a subset of country names for a plotting group.

    Parameters:
        country_names (list[str]):
            List of country names.

        group_number (int):
            Group index starting at 1.

        number_of_countries_group (int):
            Number of countries included in each group.

    Returns:
        list[str]:
            Subset of country names belonging to the selected group.

    Raises:
        ValueError:
            If `group_number` is smaller than 1.
    """
    if group_number < 1:
        raise ValueError("group_number must start at 1")

    start = (group_number - 1) * number_of_countries_group
    end = start + number_of_countries_group

    return country_names[start:end]
