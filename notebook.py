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

    return mo, pd, plt, sns


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
    print(df_change)
    return df_change, series_cols


@app.cell
def _(df_change, series_cols):
    df_change[series_cols+["year", "resistance_pct", "baseline_2018", "change_since_2018"]]
    print(df_change)
    return


@app.cell
def _(df_change):
    latest_year = df_change[df_change["year"]== 2023]
    income_summary = (latest_year.groupby("income_group").agg(n_series = ("country", "count"), mean_resistance_2018 = ("baseline_2018", "mean"), mean_resistance_2023 = ("resistance_pct", "mean"), mean_change = ("change_since_2018", "mean"), median_change = ("change_since_2018", "median")).round(2).sort_values("mean_change", ascending=False))
    print(income_summary)
    return income_summary, latest_year


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Visualize the data
    """)
    return


@app.cell
def _(df_clean, plt, sns):
    sns.histplot(data = df_clean["resistance_pct"])
    plt.title("Distribution of Resistance Percentages across all years and countries")
    plt.xlabel("Resistance Percentage")
    plt.ylabel("Count")
    plt.show()
    return


@app.cell
def _(latest_year, plt, sns):
    income_order = ["Low income", "Lower-middle income", "Upper-middle income", "High income"]
    plt.figure(figsize= (11,5))
    sns.boxplot(data = latest_year, x = "income_group", y= "change_since_2018", order = income_order, hue = "income_group")
    plt.title("Change in Antimicrobial Resistance, 2018-2023, by Income Group")
    plt.xlabel("Income Group")
    plt.ylabel("Change in Resistance since 2018 (percentage points)")
    plt.show()
    return (income_order,)


@app.cell
def _(df_change, income_order, plt, sns):
    sns.lmplot(data=df_change, x="year", y="resistance_pct", hue="income_group", hue_order=income_order, ci=None, x_jitter=0.12, height=6, aspect=1.6, legend=False)
    plt.title("Antimicrobial Resistance by Year and Income Group, 2018-2023")
    plt.xlabel("Year")
    plt.ylabel("Resistant Isolates (%)")
    plt.legend(title="Income Group", loc="center left", bbox_to_anchor=(1.02, 0.50))
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(income_summary, plt, sns):
    plt.figure(figsize=(9,5))
    sns.barplot(data=income_summary, x="income_group", y="mean_change", hue="income_group")
    plt.title("Mean Change of Antimicrobial Resistance by Income Group")
    plt.xlabel("Income Group")
    plt.ylabel("Mean Change (Percentage Points)")
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
