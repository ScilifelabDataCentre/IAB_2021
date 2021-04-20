"""This script produces the plots required for the one-pagers"""

# 5 plots required in total for each reporting facility included in the 2021 IAB report
# 3 pie charts showing users in each year 2018-2020
# 2 stacked bar plots (one for JIF score, one for type of publication: service, collab...)

# In input_data.py data is formatted accordingly
# Need to being the data across
# in colour science script, colours are given

import pandas as pd
import os
import plotly.graph_objects as go

from colour_science_2020 import (
    SCILIFE_COLOURS,
    FACILITY_USER_AFFILIATION_COLOUR_OFFICIAL,
)
from input_data import affiliate_data, pub_cat_data, JIF_data

# affiliate_data - a combined dataset of affiliates for each facility and year
# pub_cat_data - a summary of the number of each 'type' of publication for each fac and year
# JIF_data - a summary of data in JIF categories (e.g. JIF = 6-9) for each fac and year


## Create publication category plots


def pub_cat_func(input):
    pubcats = input
    # split down dataframes to enable stacking
    Collaborative = pubcats[(pubcats["Qualifiers"] == "Collaborative")]
    Service = pubcats[(pubcats["Qualifiers"] == "Service")]
    Tech_dev = pubcats[(pubcats["Qualifiers"] == "Technology development")]
    No_cat = pubcats[(pubcats["Qualifiers"] == "No category")]
    # Make stacked bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="Collaborative",
                x=Collaborative.Year,
                y=Collaborative.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[17], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="Service",
                x=Service.Year,
                y=Service.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="Technology development",
                x=Tech_dev.Year,
                y=Tech_dev.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[4], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="No category",
                x=No_cat.Year,
                y=No_cat.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)
                ),
            ),
        ]
    )

    fig.update_layout(
        barmode="stack",
        plot_bgcolor="white",
        font=dict(size=18),
        margin=dict(r=150),
        width=600,
        height=600,
        showlegend=True,
    )
    # List years to use in x-axis
    Years = pubcats["Year"].unique().astype(str)
    Years_int = pubcats["Year"].unique()
    # modify x-axis
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        ticktext=[
            "<b>" + Years[0] + "</b>",
            "<b>" + Years[1] + "</b>",
            "<b>" + Years[2] + "</b>",
        ],
        tickvals=[Years[0], Years[1], Years[2]],
    )

    Year_one = pubcats[(pubcats["Year"] == Years_int[0])]
    Year_two = pubcats[(pubcats["Year"] == Years_int[1])]
    Year_three = pubcats[(pubcats["Year"] == Years_int[2])]

    highest_y_value = max(
        Year_one["Count"].sum(), Year_two["Count"].sum(), Year_three["Count"].sum()
    )

    if highest_y_value < 10:
        yaxis_tick = 1
    if highest_y_value > 10:
        yaxis_tick = 2
    if highest_y_value > 20:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10
    if highest_y_value > 100:
        yaxis_tick = 20
    if highest_y_value > 150:
        yaxis_tick = 40
    if highest_y_value > 200:
        yaxis_tick = 50
    if highest_y_value > 1000:
        yaxis_tick = 100

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="black",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, int(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/pubcat_plots/"):
        os.mkdir("Plots/pubcat_plots/")
    fig.write_image(
        "Plots/pubcat_plots/{}_cats.png".format(
            input["Unit"][input["Unit"].first_valid_index()]
        )
    )


# function to iterate through all units for publication category/type

for i in pub_cat_data["Unit"].unique():
    print(i)
    pub_cat_func(pub_cat_data[(pub_cat_data["Unit"] == i)])


## Create JIF plots


def JIF_graph_func(input):
    JIFcounts = input
    # split down dataframes to enable stacking
    UnknownJIF = JIFcounts[(JIFcounts["JIFcat"] == "JIF unknown")]
    Undersix = JIFcounts[(JIFcounts["JIFcat"] == "JIF <6")]
    sixtonine = JIFcounts[(JIFcounts["JIFcat"] == "JIF 6-9")]
    ninetotwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF 9-25")]
    overtwentyfive = JIFcounts[(JIFcounts["JIFcat"] == "JIF >25")]
    # Make stacked bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="JIF unknown",
                x=UnknownJIF.Year,
                y=UnknownJIF.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[17], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF < 6",
                x=Undersix.Year,
                y=Undersix.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 6 - 9",
                x=sixtonine.Year,
                y=sixtonine.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[4], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF 9 - 25",
                x=ninetotwentyfive.Year,
                y=ninetotwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="JIF > 25",
                x=overtwentyfive.Year,
                y=overtwentyfive.Count,
                marker=dict(
                    color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)
                ),
            ),
        ]
    )

    fig.update_layout(
        barmode="stack",
        plot_bgcolor="white",
        font=dict(size=18),
        margin=dict(r=150),
        width=600,
        height=600,
        showlegend=True,
    )
    # List years to use in x-axis
    Years = JIFcounts["Year"].unique().astype(str)
    Years_int = JIFcounts["Year"].unique()
    # modify x-axis
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        ticktext=[
            "<b>" + Years[0] + "</b>",
            "<b>" + Years[1] + "</b>",
            "<b>" + Years[2] + "</b>",
        ],
        tickvals=[Years[0], Years[1], Years[2]],
    )

    Year_one = JIFcounts[(JIFcounts["Year"] == Years_int[0])]
    Year_two = JIFcounts[(JIFcounts["Year"] == Years_int[1])]
    Year_three = JIFcounts[(JIFcounts["Year"] == Years_int[2])]

    highest_y_value = max(
        Year_one["Count"].sum(), Year_two["Count"].sum(), Year_three["Count"].sum()
    )

    if highest_y_value < 10:
        yaxis_tick = 1
    if highest_y_value > 10:
        yaxis_tick = 2
    if highest_y_value > 20:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10
    if highest_y_value > 100:
        yaxis_tick = 20
    if highest_y_value > 150:
        yaxis_tick = 40
    if highest_y_value > 200:
        yaxis_tick = 50
    if highest_y_value > 1000:
        yaxis_tick = 100

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="black",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, int(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/JIF_plots/"):
        os.mkdir("Plots/JIF_plots/")
    fig.write_image(
        "Plots/JIF_plots/{}_JIF.png".format(
            input["Unit"][input["Unit"].first_valid_index()]
        )
    )


# function to iterate through all units for JIF

# for i in JIF_data["Unit"].unique():
#     print(i)
#     JIF_graph_func(JIF_data[(JIF_data["Unit"] == i)])
