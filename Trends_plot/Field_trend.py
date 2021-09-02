"""preliminary script considering trends over time"""

import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

trend_data = pd.read_excel(
    "Data/test_trends.xlsx",
    sheet_name="Sheet 1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

trend_group = trend_data.groupby(["Year", "Field"]).mean().reset_index()

# Each field will be a different line. Need to subset by field
Bacteria_trend = trend_group[(trend_group["Field"] == "Bacteria ")]
Protist_trend = trend_group[(trend_group["Field"] == "Protist ")]
Virus_trend = trend_group[(trend_group["Field"] == "Virus ")]
# print(Virus_trend)

colours = [
    SCILIFE_COLOURS[16],
    SCILIFE_COLOURS[17],
    SCILIFE_COLOURS[18],
]


# make figure
# fig = go.Figure()
# Add traces - each line a different trace
fig = px.scatter(
    trend_group,
    x="Year",
    y="Value",
    # set the size of the marker by impact value
    size="Value_imp",
    # set the colour of the maker by impact value
    # color="Value_imp",
    # color_continuous_scale=colours,
)
fig.update_traces(
    #    marker=dict(size=20, line=dict(width=2, color="black")),
    marker=dict(color="black", line=dict(width=2, color="black")),
    cliponaxis=False,
    opacity=1,
)
fig.add_trace(
    go.Scatter(
        name="Virus",
        x=Virus_trend.Year,
        y=Virus_trend.Value,
        mode="lines",
        marker=dict(color=SCILIFE_COLOURS[12]),
        line=dict(color=SCILIFE_COLOURS[12], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Protist",
        x=Protist_trend.Year,
        y=Protist_trend.Value,
        mode="lines",
        marker=dict(color=SCILIFE_COLOURS[0]),
        line=dict(color=SCILIFE_COLOURS[0], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Bacteria",
        x=Bacteria_trend.Year,
        y=Bacteria_trend.Value,
        mode="lines",
        marker=dict(color=SCILIFE_COLOURS[8]),
        line=dict(color=SCILIFE_COLOURS[8], width=2),
    )
)
fig.update_layout(
    plot_bgcolor="white",
    autosize=False,
    font=dict(size=18),
    margin=dict(r=250, t=0, b=0, l=0),
    width=1800,
    height=1000,
    showlegend=True,
)
fig.update_layout(
    legend=dict(
        yanchor="top",
        # y=0.99,
        xanchor="right",
        title="Field",
        x=1.1,
    )
)
# move colorbar
fig.update_layout(
    coloraxis_colorbar=dict(
        title="Impact score",
        yanchor="top",
        y=1,
        x=-0.15,
        ticks="outside",
    )
)
Years = trend_group["Year"].unique().astype(str)
Years_int = trend_group["Year"].unique()
# modify x-axis
fig.update_xaxes(
    title=" ",
    showgrid=True,
    linecolor="black",
    # add more years as needed
    ticktext=[
        "<b>" + Years[0] + "</b>",
        "<b>" + Years[1] + "</b>",
        "<b>" + Years[2] + "</b>",
        "<b>" + Years[3] + "</b>",
        "<b>" + Years[4] + "</b>",
        "<b>" + Years[5] + "</b>",
        "<b>" + Years[6] + "</b>",
        "<b>" + Years[7] + "</b>",
        #           "<b>" + Years[8] + "</b>",
    ],
    tickvals=[
        Years[0],
        Years[1],
        Years[2],
        Years[3],
        Years[4],
        Years[5],
        Years[6],
        Years[7],
        #            Years[8],
    ],
)

highest_y_value = max(trend_group["Value"])

if highest_y_value < 1:
    yaxis_tick = 0.1
if highest_y_value > 2:
    yaxis_tick = 0.2
if highest_y_value > 3:
    yaxis_tick = 0.5

fig.update_yaxes(
    title=" ",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    dtick=yaxis_tick,
    range=[0, int(highest_y_value * 1.15)],
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
# fig.show()
# fig.write_image("Plots/{}_trends.svg".format(name))
