"""generates stacked barplot with units on x-axis, 
funding amount on y-axis,
stacks divided by SciLifeLab, University funding and other funding
e.g. Figure 8 in 2020 IEC report"""

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

Facility_data = pd.read_excel(
    "Data/Single data 2020_ver3.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fund_data = pd.read_excel(
    "Data/Other funding 2020.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Facility_data.rename(
    columns={
        "Funding 2020 SciLifeLab (kSEK)": "Amount (kSEK)",
    },
    inplace=True,
)

SLL_funding = Facility_data[["Facility", "Platform", "Amount (kSEK)"]]
SLL_funding.insert(loc=2, column="Financier", value="SciLifeLab")

Funding_comb = pd.concat([SLL_funding, fund_data])


Funding_comb["Group_finance"] = Funding_comb["Financier"]


Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
    dict.fromkeys(
        [
            "Universities",
            "UU",
            "Chalmers",
            "LiU",
            "SLU",
            "LU",
            "UmU",
            "KTH",
            "SU",
            "GU",
            "KI",
            "ÖRU",
        ],
        "University",
    ),
    regex=True,
)

# Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
#     dict.fromkeys(
#         ["University hospital", "County council", "ALF"],
#         "Healthcare",
#     ),
#     regex=True,
# )

Funding_comb["Group_finance"] = Funding_comb["Group_finance"].replace(
    dict.fromkeys(
        [
            "University hospital",
            "County council",
            "ALF",
            "Elixir",
            "Nordforsk",
            "SSF",
            "Vinnova",
            "KAW",
            "VR",
        ],
        "Other",
    ),
    regex=True,
)

Funding_comb = Funding_comb.rename(columns={"Amount (kSEK)": "funds"})
Funding_comb["Mfunds"] = Funding_comb["funds"] / 1000

# check replacements#Funding_comb.to_excel("testfilefundbar.xlsx")
# check 3 categories# print(Funding_comb["Group_finance"].unique())

# group by the individual funding type (scilifelab, uni, other) and facility

Funding_summed = Funding_comb.groupby(["Facility", "Group_finance"]).sum().reset_index()

SciLifeLab_fund = Funding_summed[(Funding_summed["Group_finance"] == "SciLifeLab")]
University_fund = Funding_summed[(Funding_summed["Group_finance"] == "University")]
Other_fund = Funding_summed[(Funding_summed["Group_finance"] == "Other")]

# Make stacked bar chart
fig = go.Figure(
    data=[
        go.Bar(
            name="Other funding",
            x=Other_fund.Facility,
            y=Other_fund.Mfunds,
            marker=dict(color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="University funding",
            x=University_fund.Facility,
            y=University_fund.Mfunds,
            marker=dict(color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="SciLifeLab funding",
            x=SciLifeLab_fund.Facility,
            y=SciLifeLab_fund.Mfunds,
            marker=dict(color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)),
        ),
    ]
)

fig.update_layout(
    barmode="stack",
    plot_bgcolor="white",
    font=dict(size=18),
    autosize=False,
    margin=dict(r=0, t=0, b=0, l=0),
    width=2500,
    height=1000,
    xaxis={"categoryorder": "total descending"},
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="right", x=1),
)

# modify x-axis
fig.update_xaxes(
    title=" ",
    showgrid=True,
    linecolor="black",
)

Funding_grpmax = Funding_comb.groupby(["Facility"]).sum().reset_index()
Funding_max = max(Funding_grpmax["Mfunds"])

# modify y-axis
fig.update_yaxes(
    title="Funding (MSEK)<br>",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="black",
    linecolor="black",
    dtick=10,  # 10 will work fine with most values
    range=[0, int(Funding_max * 1.15)],
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()
fig.write_image("Plots/Unitfunding_barchart_2020.svg")
