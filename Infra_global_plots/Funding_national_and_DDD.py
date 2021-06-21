"""This script will generate a pie chart (like figure 5 in IEC report)"""

import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

df = pd.read_excel(
    "Data/Funding 2021 National.xlsx",
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

df["Category"] = df["Category"].replace(
    "Collaborations & External Relations", "Collaborations & <br>External Relations"
)
df["Category"] = df["Category"].replace(
    "Infrastructure Platforms", "Infrastructure <br>Platforms"
)
df["Category"] = df["Category"].replace("Training and courses ", "Training & courses ")
df["Category"] = df["Category"].replace(
    "Site costs, Campus Solna & Navet", "Site costs, Campus<br> Solna & Navet"
)
df["Category"] = df["Category"].replace(
    "Joint SciLifeLab Initiatives", "Joint SciLifeLab <br>Initiatives"
)


colours = [
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[17],
    SCILIFE_COLOURS[13],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[6],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[16],
    SCILIFE_COLOURS[18],
]

df["Funding (MSEK)"] = df["Funding (MSEK)"].round(1)  # .astype(int)
print(df)

fig = go.Figure(
    go.Pie(
        values=df["Funding (MSEK)"],
        labels=df["Category"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} <br>(%{value})",
)
fig.update_layout(
    margin=dict(l=100, r=100, b=100, t=100),
    font=dict(size=34),
    showlegend=False,
    width=1500,
    height=1500,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/SLL_nat_and_DDD_fund.png", scale=3)
fig.write_image("Plots/SLL_nat_and_DDD_fund.svg", scale=3)
