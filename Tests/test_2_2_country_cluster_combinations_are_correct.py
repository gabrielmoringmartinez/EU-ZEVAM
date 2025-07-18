import os
import pandas as pd

def test_country_cluster_combinations_are_correct():
    # File paths
    registrations_file = os.path.join("inputs", "1_1_new_registrations_by_fuel_type_1970_2050_clusters.csv")
    labels_file = os.path.join("inputs", "0_country_clusters.csv")

    # Load both CSVs
    registrations_df = pd.read_csv(registrations_file, delimiter=';', decimal=',')
    labels_df = pd.read_csv(labels_file, delimiter=';', decimal=',')

    # Get unique (country, cluster) pairs
    registrations_pairs = set(
        registrations_df[["geo country", "cluster"]].drop_duplicates().itertuples(index=False, name=None)
    )
    labels_pairs = set(
        labels_df[["geo country", "cluster"]].drop_duplicates().itertuples(index=False, name=None)
    )

    # Identify mismatched pairs
    missing_pairs = registrations_pairs - labels_pairs

    # Fail the test if any pairs are missing
    if missing_pairs:
        missing_str = "\n".join([f"- {country}, cluster {cluster}" for country, cluster in sorted(missing_pairs)])
        raise AssertionError(
            f"The following (geo country, cluster) combinations in '1_1_new_registrations_by_fuel_type_1970_2050_clusters' are incorrect based on '0_country_clusters.csv':\n{missing_str}"
        )