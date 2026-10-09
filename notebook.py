import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #CAI5735 Group 1 Mid-Term Project
    ##Karissa Kocourek, James Jobczynski, and Cameron Wilson

    This Marimo notebook will serve as our mid-term project collaboration, and is comprised of an executable Marimo notebook and presentation slides.

    Project Directions: Available [HERE](https://docs.google.com/document/d/1pw1L-eRHP3wGzltgrNmSBa-1lKtNe4S59MkiHHbFHsk/edit?tab=t.0).

    <b>Project submission due: October 15, 2026 at 23:59</b>
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
    df_raw = pd.read_csv("https://www.kaggle.com/datasets/hussnainmamoon1/global-antibiotic-resistance-2018-2024-glass?select=amr_global_resistance_rates.csv")
    df_raw.head()
    df_raw.shape()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
