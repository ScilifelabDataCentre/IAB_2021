""" This script will make a stacked bar chart to show interactions between infra and affiliates each year (2013-20)"""
# Fellows might need to be only 14-20
import pandas as pd
import os
import plotly.graph_objects as go

# import plotly.express as px
# import numpy as np
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

# data
interactions = pd.read_excel(
    "Data/Numbers_interact_yearly_forpyth.xlsx",
    sheet_name="Sheet 1",
    engine="openpyxl",
)


def interactions_graph_func(input, name):
    interactions = input
    # split down dataframes to enable stacking
    Infra = interactions[(interactions["Type_pub"] == "Infra")]
    affiliates = interactions[(interactions["Type_pub"] == "Aff")]
    intersect = interactions[(interactions["Type_pub"] == "Intersect")]
    # Make stacked bar chart
    fig = go.Figure(
        data=[
            go.Bar(
                name="Infrastructure Users",
                x=Infra.Year,
                y=Infra.No_pubs,
                marker=dict(
                    color=SCILIFE_COLOURS[12], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="Joint Publication",
                x=intersect.Year,
                y=intersect.No_pubs,
                marker=dict(
                    color=SCILIFE_COLOURS[8], line=dict(color="#000000", width=1)
                ),
            ),
            go.Bar(
                name="Affiliated Researchers",
                x=affiliates.Year,
                y=affiliates.No_pubs,
                marker=dict(
                    color=SCILIFE_COLOURS[0], line=dict(color="#000000", width=1)
                ),
            ),
        ]
    )

    fig.update_layout(
        barmode="stack",
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=55),  # 58 for fellows
        margin=dict(r=250, t=0, b=0, l=0),
        width=2300,
        height=1200,
        showlegend=True,
    )
    # List years to use in x-axis
    Years = interactions["Year"].unique().astype(str)
    Years_int = interactions["Year"].unique()
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

    Year_one = interactions[(interactions["Year"] == Years_int[0])]
    Year_two = interactions[(interactions["Year"] == Years_int[1])]
    Year_three = interactions[(interactions["Year"] == Years_int[2])]
    Year_four = interactions[(interactions["Year"] == Years_int[3])]
    Year_five = interactions[(interactions["Year"] == Years_int[4])]
    Year_six = interactions[(interactions["Year"] == Years_int[5])]
    Year_seven = interactions[(interactions["Year"] == Years_int[6])]
    Year_eight = interactions[(interactions["Year"] == Years_int[7])]
    #    Year_nine = interactions[(interactions["Year"] == Years_int[8])]

    highest_y_value = max(
        Year_one["No_pubs"].sum(),
        Year_two["No_pubs"].sum(),
        Year_three["No_pubs"].sum(),
        Year_four["No_pubs"].sum(),
        Year_five["No_pubs"].sum(),
        Year_six["No_pubs"].sum(),
        Year_seven["No_pubs"].sum(),
        Year_eight["No_pubs"].sum(),
        #        Year_nine["No_pubs"].sum(),
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
    if highest_y_value > 500:
        yaxis_tick = 200
    if highest_y_value > 1000:
        yaxis_tick = 200

    # modify y-axis
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
    fig.write_image("Plots/{}_1320.png".format(name))
    fig.write_image("Plots/{}_1320.svg".format(name))


# make plot by applying function

interactions_graph_func(interactions, "intersections_allyears")
