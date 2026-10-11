# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.3",
#     "matplotlib>=3.11.2",
#     "numpy>=2.5.3",
#     "pandas>=3.0.6",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #CAI5735 Group 1 Mid-Term Project
    ##Karissa Kocourek, James Jobczynski, and Cameron Wilson

    This Marimo notebook will serve as our mid-term project collaboration, and is comprised of an executable Marimo notebook and presentation slides.

    Project Directions: Available [HERE](https://docs.google.com/document/d/1pw1L-eRHP3wGzltgrNmSBa-1lKtNe4S59MkiHHbFHsk/edit?tab=t.0).

    <b>Project submission due: October 15, 2026 at 23:59</b>

    #Research Question:
    ##How did resistance change from 2018 to 2023, and did that trend differ by income group?
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Load the target dataset through pandas' read_csv, and inspect the data to show basic descriptors such as head/tail, shape, length, etc.
    """)
    return


@app.cell
def _(pd):
    df_raw = pd.read_csv("amr_global_resistance_rates.csv")
    print(f'(Rows, Columns): {df_raw.shape}')
    print()
    print(df_raw.info())
    return (df_raw,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Display the dataframe to show each column
    """)
    return


@app.cell
def _(df_raw):
    df_raw.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pare down the dataframe to columns and data of interest for future analysis and view the new dataframe.
    """)
    return


@app.cell
def _(df_raw):
    df_clean = df_raw[["record_id", "year", "country", "income_group", "pathogen", "antibiotic_class", "antibiotic_name", "resistance_pct", "total_isolates_tested", "resistant_isolates", "susceptibility_testing_coverage"]].copy()
    df_clean.tail(10)
    return (df_clean,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ensure the new dataframe doesnt have any missing data.
    """)
    return


@app.cell
def _(df_clean):
    df_clean.isna().sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add a new column calculating the mean resistance percentage for each country over all years.
    """)
    return


@app.cell
def _(df_clean):
    series_cols = ["country", "pathogen", "antibiotic_name"]
    baseline_2018 = (df_clean[df_clean["year"] == 2018][series_cols + ["resistance_pct"]].rename(columns={"resistance_pct": "baseline_2018"}))
    df_change = df_clean.merge(baseline_2018, on=series_cols, how="left")
    df_change["change_since_2018"] = (df_change["resistance_pct"] - df_change["baseline_2018"]).round(2)
    df_change
    print(df_change)
    return df_change, series_cols


@app.cell
def _(df_change, series_cols):
    df_change[series_cols+["year", "resistance_pct", "baseline_2018", "change_since_2018"]]
    print(df_change)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visualize how
    """)
    return


if __name__ == "__main__":
    app.run()
