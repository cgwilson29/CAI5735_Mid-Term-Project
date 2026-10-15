# CAI5735_Mid-Term-Project

This is the mid-term project for Group 1...

**Course:** CAI5735 — Applied Data Science in Health  
**Group:** 1  
**Group members:** Karissa Kocourek, James Jobczynski, Cameron Wilson

## Project Overview

This mid-term project explores patterns in global antimicrobial resistance (AMR) from 2018 through 2023. Using Python in a Marimo notebook, we examine how reported antibiotic resistance percentages changed over time and how the observed patterns vary across country income classifications. The analysis is descriptive and does not establish causal relationships.

## Research Question

> What is the relationship between time and antibiotic resistance rates from 2018 to 2023, and does this relationship differ across country income levels?

## Dataset

**File:** `amr_global_resistance_rates.csv`  
**Dataset source:** [Global Antibiotic Resistance 2018–2024 (GLASS), by hussnainmamoon1 on Kaggle](https://www.kaggle.com/datasets/hussnainmamoon1/global-antibiotic-resistance-2018-2024-glass)

**GitHub repository:** [cgwilson29/CAI5735_Mid-Term-Project](https://github.com/cgwilson29/CAI5735_Mid-Term-Project)  
**Marimo directory:** [View `__marimo__`](https://github.com/cgwilson29/CAI5735_Mid-Term-Project/tree/main/__marimo__)  
**Source labels in CSV:** WHO GLASS, WHO GLASS 2025 Report, ECDC EARS-Net, CDC NARMS/GLASS, WHO GLASS/JANIS, and WHO GLASS/AGAR. These are labels in the supplied data, not independently verified source citations.

The provided dataset contains **138 rows and 16 columns**, covering **20 countries**, **six pathogens**, **five antibiotics**, and **four income groups** over **2018–2023**.

Key fields used in the analysis:

| Column | Meaning |
| --- | --- |
| `year` | Observation year |
| `resistance_pct` | Percentage of tested isolates reported as resistant |
| `income_group` | Country income classification |
| `country` | Country of observation |
| `pathogen` | Bacterial pathogen |
| `antibiotic_name` | Antibiotic tested |
| `antibiotic_class` | Antibiotic class |
| `total_isolates_tested` | Number of isolates tested |

## Analysis Approach

The Marimo notebook uses **pandas**, **matplotlib**, and **seaborn** to:

1. Import and inspect the CSV.
2. Filter observations by pathogen, antibiotic, and year.
3. Group and compare observations by country, antibiotic class, and income group.
4. Create computed labels and calculate changes in resistance percentage points between 2018 and 2023.
5. Sort changes and visualize resistance patterns using line charts, bar charts, boxplots, and a scatter plot.

The presentation also includes a histogram describing the overall distribution of resistance percentages, a 2018-versus-2023 comparison, and a summary of changes by income group. Ensure the submitted notebook includes the required histogram and explanations for each code cell.

## Selected Presentation Findings

The group presentation reports that resistance rose in most of the observed country–antibiotic combinations. Its income-group comparison reports the following changes from 2018 to 2023:

| Income group | Average change | Median change |
| --- | ---: | ---: |
| Lower-middle income | +10.2 percentage points | +7.7 percentage points |
| Upper-middle income | +5.2 percentage points | +5.1 percentage points |
| High income | −1.4 percentage points | −0.4 percentage points |
| Low income (Ethiopia only) | +11.4 percentage points | +11.4 percentage points |

These figures are reported in the presentation and should be interpreted as descriptive results for this dataset, not estimates for all countries. The slide deck also highlights changes in resistance to ciprofloxacin, imipenem, ceftriaxone, cefotaxime, and methicillin (MRSA).

## How to Run the Analysis

**Requirements:** Python 3 and the following packages: `marimo`, `pandas`, `matplotlib`, and `seaborn`.

1. Clone or download the [GitHub repository](https://github.com/cgwilson29/CAI5735_Mid-Term-Project).
2. Open a terminal in the folder containing `analysis.py` and `amr_global_resistance_rates.csv`.
3. Install the dependencies:

   ```bash
   python -m pip install marimo pandas matplotlib seaborn
   ```

4. Launch the interactive notebook:

   ```bash
   marimo edit analysis.py
   ```

5. Open the local URL shown in the terminal to view and run the notebook.

**Important:** The CSV must remain in the same working directory as `analysis.py`, because the notebook loads it using a relative filename.

## Repository Files

```text
CAI5735_Mid-Term-Project/
├── README.md
├── analysis.py
└── amr_global_resistance_rates.csv
```

The slideshow and PDF exports may also be included if the group chooses to publish them. Follow the course instructions for submitting the notebook and slideshow PDFs to Canvas.

## Interpretation and Limitations

This is an exploratory analysis of the observations in the supplied dataset. Countries and income groups are unevenly represented, and observations cover different pathogen–antibiotic combinations. Consequently, comparisons of pooled resistance rates between income groups may be influenced by the combinations represented. Findings should not be interpreted as nationally representative estimates, proof of causation, or statistically significant differences without further analysis.

## Course Submission

The course requires a Marimo notebook and slideshow submitted as PDFs, with every group member named in both. The notebook must also contain a comment linking to this GitHub repository.

**Repository URL:** https://github.com/cgwilson29/CAI5735_Mid-Term-Project
