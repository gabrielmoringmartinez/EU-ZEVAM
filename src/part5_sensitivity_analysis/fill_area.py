def fill_area(ax, df, x_label, y_label):
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] > df[y_label[1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[-1]], where=(df[y_label[0]] <= df[y_label[-1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax

def fill_area_historical_values(ax, df, x_label, y_label):
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] <= df[y_label[1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[-1]], where=(df[y_label[0]] <= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[1]], df[y_label[-1]], where=(df[y_label[1]] <= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[1]], where=(df[y_label[0]] > df[y_label[1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax

def fill_area_increase_decrease(ax, df, x_label, y_label):
    ref_line_pos = len(y_label) // 2
    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[ref_line_pos]], where=(df[y_label[ref_line_pos]] < df[y_label[0]]),
        interpolate=True, color="green", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[ref_line_pos]], df[y_label[-1]], where=(df[y_label[ref_line_pos]] >= df[y_label[-1]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[0]], df[y_label[ref_line_pos]], where=(df[y_label[ref_line_pos]] > df[y_label[0]]),
        interpolate=True, color="red", alpha=0.25)

    ax.fill_between(
        df[x_label], df[y_label[ref_line_pos]], df[y_label[-1]], where=(df[y_label[ref_line_pos]] <= df[y_label[-1]]),
        interpolate=True, color="green", alpha=0.25)
    return ax