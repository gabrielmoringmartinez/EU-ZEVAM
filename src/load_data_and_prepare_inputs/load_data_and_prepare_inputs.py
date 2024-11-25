from src.load_data_and_prepare_inputs.load_data import load_data
from src.load_data_and_prepare_inputs.prepare_inputs import prepare_inputs


def load_data_and_prepare_inputs():
    data = load_data()
    inputs = prepare_inputs()
    return data, inputs