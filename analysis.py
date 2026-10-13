import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("amr_gloabal_resistance_rates.csv")
    df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
