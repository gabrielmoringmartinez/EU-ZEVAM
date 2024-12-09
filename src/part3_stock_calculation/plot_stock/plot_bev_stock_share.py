from src.part2_survival_rates.plot_survival_rates.plot_all_countries import plot_all_countries


def plot_bev_stock_shares(stock_shares, config_scenario):
    columns_to_plot = {'share': 'share'}
    bev_stock_shares = stock_shares[stock_shares['powertrain'] == 'BEV']
    plot_all_countries(bev_stock_shares, config_scenario, columns_to_plot, None)

