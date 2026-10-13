# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.3",
#     "matplotlib>=3.11.2",
#     "pandas>=3.0.6",
#     "seaborn>=0.13.2",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell
def _(pd):
    df = pd.read_csv("amr_global_resistance_rates.csv")
    df
    return (df,)


@app.cell
def _(df):
    resist = df.assign(label=df["country"] + " (" + df["antibiotic_name"] + ")")
    resist
    return (resist,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistance Over Time - E. Coli**
    """)
    return


@app.cell
def _(plt, resist, sns):
    ecoli = resist[resist["pathogen"] == "Escherichia coli"]

    sns.lineplot(data=ecoli, x="year", y="resistance_pct", hue="label", errorbar=None)
    plt.title("E. coli Resistance Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country (antibiotic)", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Klebsiella Pneumoniae**
    """)
    return


@app.cell
def _(plt, resist, sns):
    klebsiella = resist[resist["pathogen"] == "Klebsiella pneumoniae"]

    sns.lineplot(data=klebsiella, x="year", y="resistance_pct", hue="label", errorbar=None)
    plt.title("Klebsiella pneumoniae Resistance Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country (antibiotic)", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Staphylococcus aureus (MRSA)**
    """)
    return


@app.cell
def _(plt, resist, sns):
    staph = resist[resist["pathogen"] == "Staphylococcus aureus"]

    sns.lineplot(data=staph, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Staphylococcus aureus (MRSA) Resistance Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Acinetobacter**
    """)
    return


@app.cell
def _(plt, resist, sns):
    acinetobacter = resist[resist["pathogen"] == "Acinetobacter spp."]

    sns.lineplot(data=acinetobacter, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Acinetobacter Resistance to Imipenem Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Salmonella**
    """)
    return


@app.cell
def _(plt, resist, sns):
    salmonella = resist[resist["pathogen"] == "Salmonella spp."]

    sns.lineplot(data=salmonella, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Salmonella Resistance to Ciprofloxacin Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country", loc="upper left")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Shigella**
    """)
    return


@app.cell
def _(plt, resist, sns):
    shigella = resist[resist["pathogen"] == "Shigella spp."]

    sns.lineplot(data=shigella, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Shigella Resistance to Ciprofloxacin Over Time")
    plt.xlabel("Year")
    plt.ylabel("% resistant")
    plt.legend(title="Country", loc="upper left")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Change In Resistance from 2018 to 2023**
    """)
    return


@app.cell
def _(resist):
    wide = resist.pivot_table(index="label", columns="year", values="resistance_pct")
    change = (wide[2023] - wide[2018]).round(1).reset_index(name="change_pts")
    change["direction"] = (change["change_pts"] > 0).map({True: "Rising", False: "Falling"})
    change = change.sort_values("change_pts")
    change
    return (change,)


@app.cell
def _(change, plt, sns):
    plt.figure(figsize=(9, 8))
    sns.barplot(data=change, x="change_pts", y="label", hue="direction", palette={"Rising": "red", "Falling": "blue"})
    plt.axvline(0, color="gray")
    plt.title("Change in Resistance, 2018 to 2023")
    plt.xlabel("Change in Percent Resistant")
    plt.ylabel("")
    plt.legend(title="Direction", loc="lower right")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Resistance by Income Group in 2023**
    """)
    return


@app.cell
def _(plt, resist, sns):
    resist_2023 = resist[resist["year"] == 2023]

    plt.figure(figsize=(9, 5))
    sns.boxplot(
        data=resist_2023,
        x="income_group",
        y="resistance_pct",
        hue="income_group",
        order=["Low income", "Lower-middle income", "Upper-middle income", "High income"],
    )
    plt.title("Antibiotic Resistance by Income Group, 2023")
    plt.xlabel("")
    plt.ylabel("% resistant")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **E. Coli vs Ciprofloxacin in 2023**
    """)
    return


@app.cell
def _(plt, resist, sns):
    ecoli_cipro_2023 = resist[
        (resist["pathogen"] == "Escherichia coli")
        & (resist["antibiotic_name"] == "Ciprofloxacin")
        & (resist["year"] == 2023)
    ].sort_values("resistance_pct")

    sns.barplot(data=ecoli_cipro_2023, x="resistance_pct", y="country", hue="income_group", dodge=False)
    plt.title("E. coli Resistance to Ciprofloxacin, 2023")
    plt.xlabel("% resistant")
    plt.ylabel("")
    plt.legend(title="Income group", loc="lower right")
    plt.show()
    return


if __name__ == "__main__":
    app.run()
