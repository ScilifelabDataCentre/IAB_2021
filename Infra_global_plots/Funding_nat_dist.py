"""This script will generate a pie chart (like figure 4b in previous IAB report)"""

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

df = pd.read_excel(
    "Data/Funding 2021 Universities.xlsx",
    sheet_name="Funding Univ. 2021 mod",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

df.rename(
    columns={
        "Funding 2021 (MSEK)": "Funding (MSEK)",
    },
    inplace=True,
)

uni_map = {
    "Uppsala University": "UU",
    "Karolinska Institutet": "KI",
    "Royal Institute of Technology": "KTH",
    "Stockholm University": "SU",
    "Umeå University": "UmU",
    "University of Gothenburg": "GU",
    "Lund University": "LU",
    "Chalmers University of Technology": "Chalmers",
    "Linköping University": "LiU",
    "Swedish University of Agricultural Sciences": "SLU",
    "Örebro University": "ORU",
}

df_basic = df.replace(uni_map, regex=True)


colours = [
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[17],
    SCILIFE_COLOURS[13],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[5],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[16],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[7],
]

df_basic["Funding (MSEK)"] = df_basic["Funding (MSEK)"].round().astype(int)
# print(df_basic)

fig = go.Figure(
    go.Pie(
        values=df_basic["Funding (MSEK)"],
        labels=df_basic["University"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} (%{value})",
)
fig.update_layout(
    margin=dict(l=100, r=100, b=100, t=100),
    font=dict(size=42),
    showlegend=False,
    width=1500,
    height=1500,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/dist_nat_fund_20.png", scale=3)
fig.write_image("Plots/dist_nat_fund_20.svg", scale=3)
