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

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    # Import the necessary functions to run the notebook, including marimo, pandas and numpy for analysis/calculations, matplotlib.pyplot and seaborn for visualizations.
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    return mo, pd, plt, sns


@app.cell
def _(pd):
    # Use pd.read_csv to import the target datafile for analysis and call the dataframe to review the columns for inspection.
    df = pd.read_csv("amr_global_resistance_rates.csv")
    df
    return (df,)


@app.cell
def _(df):
    # Add a column to the dataframe combining the country name and antibiotic name.
    resist = df.assign(label=df["country"] + " (" + df["antibiotic_name"] + ")")
    resist
    return (resist,)


@app.cell
def _(df):
    # Inspect the dataframe using standardized functions: .info() combines indexes, column names, non-null counts, and data types into a single table for review.
    df.info()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistance Over Time - E. Coli**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### E. coli
    E. coli resistance is rising in most of the countries in the analysis. India has the highest rate, with 74.1% resistant to ciprofloxacin in 2023, an increase from 67.2% in 2018. Pakistan increased the most, from 55.4% to 63.1% resistance to ceftriaxone, followed by Nigeria with a 48.3% to 55.7% increase. In contrast, Sweden (9.4%), Australia (11.0%), and Germany (20.9%) did not have as drastic of an increase. Germany was the only country where E. coli resistance decreased.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Klebsiella Pneumoniae**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### Klebsiella pneumoniae
    Most Klebsiella results measure resistance to imipenem, a carbapenem antibiotic usually saved for more serious infections when other medications fail. Indonesia (28.4% to 41.2%) and India (13.5% to 25.8%) increased the most, with India's rate nearly doubling in six years. South Africa had the highest rate of 59.2%, but South Africa was tested against a different antibiotic, cefotaxime. Italy was the only country to improve with resistance over time, falling from 32.5% in 2020 to 27.3% in 2023.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Staphylococcus aureus (MRSA)**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### Staphylococcus aureus (MRSA)
    MRSA shows a clear split between countries. Japan had the largest improvement in the dataset, decreasing from 48.2% to 38.6%, and Germany decreased from 12.6% to 9.3%. Meanwhile, Pakistan increased from 37.2% to 41.4% and Kenya increased from 29.4% to 34.0%. Japan still has a higher resistance than Germany, which shows that a country can be improving while still having a high rate.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Acinetobacter**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### Acinetobacter
    Acinetobacter has some of the highest resistance rates in the dataset. More than half of the samples were resistant to imipenem in both countries by 2023: Egypt increased from 62.4% to 70.2% and Brazil from 48.2% to 56.2%. Because imipenem is a last-resort antibiotic, these rates mean doctors have very few treatment options left for these infections.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Salmonella**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### Salmonella
    Only Ethiopia has Salmonella data, so it can't be compared with other countries. Ethiopia's resistance to ciprofloxacin nearly doubled, from 12.4% in 2018 to 23.8% in 2023, rising steadily every year.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistence Over Time - Shigella**
    Create a lineplot showing the resistance trends over time, colorcoded by country, based on each bacterial species.
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


@app.cell
def _(mo):
    mo.md("""
    ### Shigella
    Only Bangladesh has Shigella data. Its resistance to ciprofloxacin increased from 18.5% to 46.8%. This is the fastest increase in the entire dataset, and the rate grew more than 2.5 times in six years.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Change In Resistance from 2018 to 2023**
    Create a table comparing the difference in resistance percent from 2018 to 2023 and label each as rising or falling based on whether the difference is positive or negative. Then create a barplot to visualize the sorted outcome.
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


@app.cell
def _(mo):
    mo.md("""
    ### Change in Resistance, 2018 to 2023
    Resistance increased in 19 of the 23 country and antibiotic combinations. The four countries that had decreased resistance were Japan (MRSA), Germany (MRSA), Italy (Klebsiella), and Germany (E. coli), all high-income countries. The largest increases were in lower-middle income countries: Bangladesh (Shigella, +28.3 points), Indonesia (Klebsiella, +12.8 points), and India (Klebsiella, +12.3 points).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Resistance by Income Group in 2023**
    Create a boxplot to visualize the 2023 antibiotic resistance by income group.
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


@app.cell
def _(mo):
    mo.md("""
    ### Resistance by Income Group, 2023
    High-income countries had much lower resistance, with a median of about 12%, compared with about 47% for lower-middle income countries and 48% for upper-middle income countries. Japan's MRSA rate (38.6%) is an outlier among high-income countries. The low-income group contains only one country (Ethiopia), so it can't be used to draw conclusions about low-income countries.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **E. Coli Resistance to Ciprofloxacin in 2023**
    Create a barplot showing the 2023 antibiotic resistance of E. coli to ciprofloxacin.
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


@app.cell
def _(mo):
    mo.md("""
    ### Comparing Countries Fairly: E. coli and Ciprofloxacin, 2023
    All five countries were tested on the same bacteria and the same antibiotic. Resistance follows income level closely: lower-middle income India (74.1%) and Nigeria (55.7%) were highest, upper-middle income Mexico (43.5%) was in the middle, and high-income Germany (20.9%) and Sweden (9.4%) were lowest. India's resistance rate is almost eight times higher than Sweden's.
    """)
    return


@app.cell
def _(resist):
    # Add a column joining the country and pathogen for future identification.
    resist_by_drug = resist.assign(country_bacteria=resist["country"] + " (" + resist["pathogen"] + ")")
    resist_by_drug
    return (resist_by_drug,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Fluoroquinolones (ciprofloxacin)**
    Create a lineplot showing antibiotic resistance of of ciprofloxacin over time.
    """)
    return


@app.cell
def _(plt, resist_by_drug, sns):
    fluoroquinolones = resist_by_drug[resist_by_drug["antibiotic_class"] == "Fluoroquinolones"]

    sns.lineplot(data=fluoroquinolones, x="year", y="resistance_pct", hue="country_bacteria", errorbar=None)
    plt.title("Resistance to Fluoroquinolones (Ciprofloxacin) Over Time")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.legend(title="Country (bacteria)", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Carbapenems (imipenem)**
    Create a lineplot showing antibiotic resistance of of imipenem over time.
    """)
    return


@app.cell
def _(plt, resist_by_drug, sns):
    carbapenems = resist_by_drug[resist_by_drug["antibiotic_class"] == "Carbapenems"]

    sns.lineplot(data=carbapenems, x="year", y="resistance_pct", hue="country_bacteria", errorbar=None)
    plt.title("Resistance to Carbapenems (Imipenem) Over Time")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.legend(title="Country (bacteria)", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **3rd-generation cephalosporins (ceftriaxone and cefotaxime)**
    Create a lineplot showing antibiotic resistance of of cephalosporins over time.
    """)
    return


@app.cell
def _(plt, resist_by_drug, sns):
    cephalosporins = resist_by_drug[resist_by_drug["antibiotic_class"] == "3rd-Gen Cephalosporins"]

    sns.lineplot(data=cephalosporins, x="year", y="resistance_pct", hue="country_bacteria", errorbar=None)
    plt.title("Resistance to 3rd-Generation Cephalosporins Over Time")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.legend(title="Country (bacteria)", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Methicillin (MRSA)**
    Create a lineplot showing antibiotic resistance of of methicillin over time.
    """)
    return


@app.cell
def _(plt, resist_by_drug, sns):
    methicillin = resist_by_drug[resist_by_drug["antibiotic_class"] == "Methicillin"]

    sns.lineplot(data=methicillin, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Methicillin (MRSA) Over Time")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **All four antibiotic classes on one chart**
    Create a lineplot showing antibiotic resistance of all antibiotic classes over time on a single chart.
    """)
    return


@app.cell
def _(plt, resist_by_drug, sns):
    sns.lineplot(data=resist_by_drug, x="year", y="resistance_pct", hue="antibiotic_class", errorbar=None)
    plt.title("Average Resistance by Antibiotic Class Over Time")
    plt.xlabel("Year")
    plt.ylabel("Average Percent Resistant")
    plt.legend(title="Antibiotic class", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell
def _(resist_by_drug):
    # Filter the data to include only 2023 data, then generate a boxplot and barplot of resistance by antibiotic class.
    drug_2023 = resist_by_drug[resist_by_drug["year"] == 2023]
    drug_2023
    return (drug_2023,)


@app.cell
def _(drug_2023, plt, sns):
    sns.boxplot(
        data=drug_2023,
        x="antibiotic_class",
        y="resistance_pct",
        hue="antibiotic_class",
        order=["Fluoroquinolones", "Carbapenems", "3rd-Gen Cephalosporins", "Methicillin"],
    )
    plt.title("Antibiotic Resistance by Antibiotic Class, 2023")
    plt.xlabel("Antibiotic class")
    plt.ylabel("Percent Resistant")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Average Resistance by Antibiotic Class**
    """)
    return


@app.cell
def _(drug_2023, plt, sns):
    sns.barplot(data=drug_2023, x="antibiotic_class", y="resistance_pct", hue="antibiotic_class", errorbar=None)
    plt.title("Average Resistance by Antibiotic Class, 2023")
    plt.xlabel("Antibiotic class")
    plt.ylabel("Average Percent Resistant")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Samples Tested vs. Resistance**
    Create a scatterplot showing the number of samples tested versus antibiotic resistance in 2023.
    """)
    return


@app.cell
def _(drug_2023, plt, sns):
    sns.scatterplot(data=drug_2023, x="total_isolates_tested", y="resistance_pct", hue="income_group")
    plt.xscale("log")
    plt.title("Samples Tested vs. Resistance, 2023")
    plt.xlabel("Number of samples tested (log scale)")
    plt.ylabel("Percent Resistant")
    plt.legend(title="Income group", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ciprofloxacin
    Create a lineplot to trend the antibiotic resistance to Ciprofloxacin over time, by country.
    """)
    return


@app.cell
def _(plt, resist, sns):
    cipro = resist[resist["antibiotic_name"] == "Ciprofloxacin"]

    sns.lineplot(data=cipro, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Ciprofloxacin, 2018 to 2023")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.xlim(2018, 2023)
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Imipenem
    Create a lineplot to trend the antibiotic resistance to imipenem over time, by country.
    """)
    return


@app.cell
def _(plt, resist, sns):
    imipenem = resist[resist["antibiotic_name"] == "Imipenem"]

    sns.lineplot(data=imipenem, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Imipenem, 2018 to 2023")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.xlim(2018, 2023)
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Ceftriaxone
    Create a lineplot to trend the antibiotic resistance to ceftriaxone over time, by country.
    """)
    return


@app.cell
def _(plt, resist, sns):
    ceftriaxone = resist[resist["antibiotic_name"] == "Ceftriaxone"]

    sns.lineplot(data=ceftriaxone, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Ceftriaxone, 2018 to 2023")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.xlim(2018, 2023)
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Cefotaxime
    Create a lineplot to trend the antibiotic resistance to cefotaxime over time, by country.
    """)
    return


@app.cell
def _(plt, resist, sns):
    cefotaxime = resist[resist["antibiotic_name"] == "Cefotaxime"]

    sns.lineplot(data=cefotaxime, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Cefotaxime, 2018 to 2023")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.xlim(2018, 2023)
    plt.legend(title="Country", loc="upper left")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Methicillin (MRSA)
    Create a lineplot to trend the antibiotic resistance to methicillin over time, by country.
    """)
    return


@app.cell
def _(plt, resist, sns):
    mrsa = resist[resist["antibiotic_name"] == "Methicillin (MRSA)"]

    sns.lineplot(data=mrsa, x="year", y="resistance_pct", hue="country", errorbar=None)
    plt.title("Resistance to Methicillin (MRSA), 2018 to 2023")
    plt.xlabel("Year")
    plt.ylabel("Percent Resistant")
    plt.xlim(2018, 2023)
    plt.legend(title="Country", bbox_to_anchor=(1, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Antibiotic Resistance in 2018 vs. 2023**
    Create a scatterplot comparing each country and antibiotic's resistance in 2018 to 2023, colorcoded by income group. Points above the dashed line increased in resistance.
    """)
    return


@app.cell
def _(plt, resist, sns):
    # Pivot so each country/antibiotic pair has its 2018 and 2023 values side by side, keeping income group for color.
    scatter_wide = resist.pivot_table(index=["label", "income_group"], columns="year", values="resistance_pct").reset_index()

    sns.scatterplot(
        data=scatter_wide,
        x=2018,
        y=2023,
        hue="income_group",
        hue_order=["Low income", "Lower-middle income", "Upper-middle income", "High income"],
        s=60,
    )
    plt.plot([0, 80], [0, 80], linestyle="--", color="gray", label="No change")
    plt.xlim(0, 80)
    plt.ylim(0, 80)
    plt.title("Antibiotic Resistance in 2018 vs. 2023")
    plt.xlabel("Percent Resistant in 2018")
    plt.ylabel("Percent Resistant in 2023")
    plt.legend(title="Income group", bbox_to_anchor=(1, 1))
    plt.show()
    return


if __name__ == "__main__":
    app.run()
