import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def plot_survival_rate_country(ax, label, x, y, country_name, plot_params, i):
    ax.plot(x, y, '-o', markersize=plot_params["marker_size"], linewidth=plot_params["line_width"], label=label)
    if i == 2:
        ax.legend(fontsize=plot_params["legend_fontsize"])
    ax.set_title(country_name, fontsize=plot_params["title_fontsize"])
    plt.style.use('seaborn-v0_8-white')
    ax = plt.gca()
    customize_axes(ax, plot_params["show_grid"])


def customize_axes(ax, show_grid):
    ax.grid(show_grid)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
    ax.set_xlim(0, 45)
    ax.set_ylim(0, None)
    y_ticks = ax.get_yticks()
    ax.set_yticks([0] + y_ticks[y_ticks != 0])
    x_ticks = ax.get_xticks()
    return ax