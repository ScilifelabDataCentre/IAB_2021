"""This script will generate a pie chart (like figure 10 in 2020 IEC report)"""

# Note: potentially need to trim original file from OO
# Has 'spare' rows, columns and totals for checking
import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

Acaduser_data = pd.read_excel(
    "Data/Academic user distribution 2020.xlsx",
    sheet_name="Academic Users 2020",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


colours = [
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[1],
    SCILIFE_COLOURS[15],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[9],
    SCILIFE_COLOURS[16],
    SCILIFE_COLOURS[17],
]

# Edited this to fit more nicely
Acaduser_data["Academic User affiliation"] = Acaduser_data[
    "Academic User affiliation"
].replace(
    "Swedish University of Agricultural Sciences",
    "Swedish University of <br>Agricultural Sciences",
)


fig = go.Figure(
    go.Pie(
        values=Acaduser_data["Percent"],
        labels=Acaduser_data["Academic User affiliation"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} <br>(%{percent})",
)
fig.update_layout(
    margin=dict(l=200, r=200, b=200, t=200),
    font=dict(size=18),
    showlegend=False,
    width=1000,
    height=1000,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/Acaduser_data_pie.svg", scale=3)
