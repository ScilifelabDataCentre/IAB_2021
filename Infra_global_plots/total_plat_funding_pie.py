"""This script will generate a pie chart (like figure 10 in 2020 IEC report)"""

# Note: potentially need to trim original file from OO
# Has 'spare' rows, columns and totals for checking
import pandas as pd
import plotly.graph_objects as go
import os
import numpy as np
from colour_science_2020 import (
    PLATFORM_FUNDING_COLOURS,
)

Plat_tot_fund_data = pd.read_excel(
    "Data/Total_platform_funding.xlsx",
    sheet_name="Sheet 1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# OO requested percentages rounded to nearest percent for this graph
Plat_tot_fund_data["Fund_MSEK"] = Plat_tot_fund_data["Funding"] / 1000
# print(Acaduser_data)
colours = np.array([""] * len(Plat_tot_fund_data["Funder"]), dtype=object)
for i in Plat_tot_fund_data["Funder"]:
    colours[np.where(Plat_tot_fund_data["Funder"] == i)] = PLATFORM_FUNDING_COLOURS[
        str(i)
    ]

Plat_tot_fund_data["Funder"] = Plat_tot_fund_data["Funder"].replace(
    "SciLifeLab Base",
    "SciLifeLab<br>Base<br>",
)
Plat_tot_fund_data["Funder"] = Plat_tot_fund_data["Funder"].replace(
    "SciLifeLab Instrument",
    "SciLifeLab Instrument<br>",
)
Plat_tot_fund_data["Funder"] = Plat_tot_fund_data["Funder"].replace(
    "Healthcare",
    "Healthcare<br>",
)
Plat_tot_fund_data["Funder"] = Plat_tot_fund_data["Funder"].replace(
    "KAW",
    "KAW<br>",
)
Plat_tot_fund_data["Funder"] = Plat_tot_fund_data["Funder"].replace(
    "VR",
    "VR<br>",
)


fig = go.Figure(
    go.Pie(
        values=Plat_tot_fund_data["Fund_MSEK"],
        labels=Plat_tot_fund_data["Funder"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} (%{value:.1f})",
)
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    font=dict(size=34),
    annotations=[
        dict(
            showarrow=False,
            text="{}".format(round(sum(Plat_tot_fund_data["Fund_MSEK"]), 1)),
            font=dict(size=50),  # should work for all centre bits
            x=0.5,
            y=0.5,
        )
    ],
    # paper_bgcolor="rgba(0,0,0,0)",
    # plot_bgcolor="rgba(0,0,0,0)",
    showlegend=False,
    width=1000,
    height=1000,
    autosize=False,
)
if not os.path.isdir("Plots/Platform_fund_pies/"):
    os.mkdir("Plots/Platform_fund_pies/")
fig.show()
fig.write_image("Plots/Platform_fund_pies/total platform funding.svg", scale=3)
fig.write_image("Plots/Platform_fund_pies/total platform funding.png", scale=3)
