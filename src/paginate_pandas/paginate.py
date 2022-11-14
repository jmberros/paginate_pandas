from typing import Union

import pandas as pd
import ipywidgets


def paginate(
    df: Union[pd.Series, pd.DataFrame],
    page_size: int = 15,
    page: int = 1,
    fillna_with_empty_string: bool = False,
):
    """Creates an interactive paginator for a pandas Series or DataFrame.

    Args:
        df: A pandas.Series or DataFrame.
        page_size: The number of rows to display per page.
        page: The initial page to show.
        fillna_with_empty_string: Fills NaNs with empty strings for better
            visualization.
    """
    if len(df.shape) == 1:
        n = df.shape
        m = 1
    else:
        n, m = df.shape

    pd.options.display.max_rows = n
    print(f"{n:,} rows, {m:,} columns")

    def _paginate_df(page):
        i = page - 1
        ix_start = min(i * page_size, n)
        ix_stop = min((i + 1) * page_size, n)
        df_page = df.iloc[ix_start:ix_stop]
        return df_page.fillna("") if fillna_with_empty_string else df_page

    last_page, remainder = divmod(n, page_size)
    if remainder:
        last_page += 1

    if last_page > 1:
        ipywidgets.interact(
            _paginate_df,
            page=ipywidgets.widgets.IntSlider(
                min=1, max=last_page, step=1, value=page,
                description=f"Total pages: {last_page:,}",
                style={"description_width": "initial"},
                readout_format=",",
            ),
        )
    else:
        return df  # No pagination needed


def paginate_fillna(df, page_size=15, page=1):
    """Paginates filliing NaNs with empty strings.

    See `paginate` docstring.
    """
    return paginate(df, page_size=page_size, page=page, fillna_with_empty_string=True)
