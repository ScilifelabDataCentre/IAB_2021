"""creates scatterplot of funding(log10) (x), publications(log10) (y), points coloured by platform"""

import pandas as pd
import numpy as np
import os
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)
from input_data import fac_map

# Get total funding data (platform and unit info also needed)
Facility_data = pd.read_excel(
    "Data/Single data 2020_ver3.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

other_funding = pd.read_excel(
    "Data/Other funding 2020.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Some funding info also included in the facility data
# extract SLL funding data from single(facility) data

Facility_data.rename(
    columns={
        "Funding 2020 SciLifeLab (kSEK)": "Amount (kSEK)",
    },
    inplace=True,
)


SLL_funding = Facility_data[["Facility", "Platform", "Amount (kSEK)"]]
SLL_funding.insert(loc=2, column="Financier", value="SciLifeLab")

# now concatenate this with other funding
# calculate total funding
Funding_comb = pd.concat([SLL_funding, other_funding])
tot_fund = Funding_comb.groupby(["Facility", "Platform"]).sum().reset_index()
tot_fund.insert(loc=3, column="SEK", value=(tot_fund["Amount (kSEK)"] * 1000))
tot_fund = tot_fund.drop(
    [
        "Amount (kSEK)",
    ],
    axis=1,
)
# need to check how exactly the funding values were included in the plots

# need publications data (easier to have individual labels for units)
# Note only want for latest year - in IAB 2021, that's 2020
Pub_data = pd.read_excel(
    "Data/Pub_18to20_indivlab_20210415.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Now calculate total number of publications for each unit in 2020
Pub_data_2020 = Pub_data[Pub_data["Year"] == 2020]
# Need to convert names so that counts of pubs can be joined with funding
# can import this information from input_data (script originally used for one-pagers, but appropriate portion also in this repository section)

Pub_data_20_sub = Pub_data_2020.drop(
    [
        "Authors",
        "Journal",
        "ISSN",
        "ISSN-L",
        "Year",
        "Published",
        "E-published",
        "Volume",
        "Issue",
        "Pages",
        "DOI",
        "PMID",
        "Qualifiers",
        "IUID",
        "URL",
        "DOI URL",
        "PubMed URL",
        "QC",
    ],
    axis=1,
)
Pub_data_20_sub["Labels"] = Pub_data_20_sub["Labels"].str.replace(
    r"\(.*\)", "", regex=True
)
Pub_data_20_sub["Labels"] = Pub_data_20_sub["Labels"].str.replace(
    "High-throughput Genome Engineering ",
    "High Throughput Genome Engineering",
    regex=True,
)
Pub_data_20_sub = Pub_data_20_sub.replace(fac_map, regex=True)

count_pub = Pub_data_20_sub.groupby(["Labels"]).count().reset_index()
count_pub.rename(
    columns={"Labels": "Facility", "Title": "Count"},
    inplace=True,
)

pubs_fund_data = pd.merge(
    tot_fund,
    count_pub,
    how="left",
    left_on="Facility",
    right_on="Facility",
)
# most of the units with Nan in publications have none, so replace with 0
# HOWEVER, this is not true for Mass cytometry, fo which publication data is combined
pubs_fund_data.loc[22, "Count"] = 20
# For the above, I checked the number of publications for Mass Cytometry (LiU)
# and set the appropriate value (20) to the row for Mass Cytometry (KI) in the 'Count' column
# OO requested that units with no publications were dropped (might drop anyway with log, but ensuring that they are dropped)
pubs_fund_data.dropna(subset=["Count"], inplace=True)
print(pubs_fund_data)
pubs_fund_data["log_Count"] = np.log10(pubs_fund_data["Count"])
pubs_fund_data["log_Fund"] = np.log10(pubs_fund_data["SEK"])
# OO needs 2 versions - compute and storage is an outlier, so need one fig with it and one without
pubs_fund_data = pubs_fund_data[
    ~pubs_fund_data.Facility.str.contains("Compute and Storage")
]
# comment out the above to include compute and storage

colours = [
    SCILIFE_COLOURS[1],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[17],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[15],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[9],
    SCILIFE_COLOURS[16],
]

# Now to plot this as a scatter plot
fig = px.scatter(
    pubs_fund_data,
    x="log_Fund",
    y="log_Count",
    color="Platform",
    color_discrete_sequence=colours,
)

fig.update_traces(
    marker=dict(size=20, line=dict(width=2, color="black")), cliponaxis=False
)

fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=18),
    margin=dict(r=0, t=0, b=0, l=0),
    width=2500,
    height=1000,
    showlegend=True,
    legend=dict(
        title=" ", orientation="h", yanchor="bottom", y=1, xanchor="right", x=1
    ),
)

# modify x-axis
fig.update_xaxes(
    title="Total Funding (log10)",
    showgrid=True,
    linecolor="black",
)

max_pubs = max(pubs_fund_data["log_Count"])

# modify y-axis
fig.update_yaxes(
    title="Publications (log10)<br>",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="black",
    linecolor="black",
    range=[0, max_pubs * 1.15],
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")

# fig.show()
# fig.write_image("Plots/Fund_pub_scatter_noCS.svg", scale=3)
