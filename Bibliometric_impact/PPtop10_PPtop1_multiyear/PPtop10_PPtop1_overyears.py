"""this script considers how PP(top10) and PP(top1) change over time for each group of publications -
fellows, units and affiliates"""
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px

# from colour_science_2020 import (
#     SCILIFE_COLOURS,
# )

## top10_scxw0 - data for PP(top10) - proportion of papers in the top 10% most cited
# top1_scxw0 - data for PP(top1) - proportion of papers in the top 1% most cited

### Fellows data prep

Fellows_data = pd.read_excel(
    "Data/SciLifeLab-fellows-20210512.xlsx",
    sheet_name="publ_info",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Fellows_data_sub = Fellows_data[
    (Fellows_data["Publication_year"] > 2013)
    & (Fellows_data["Publication_year"] < 2019)
]

Fellows_data_sub = Fellows_data_sub[
    Fellows_data_sub["top10_scxw0"].str.contains("None") == False
]

Fellows_data_sub["top10_scxw0"] = Fellows_data_sub["top10_scxw0"].astype(float)
Fellows_data_sub["top1_scxw0"] = Fellows_data_sub["top1_scxw0"].astype(float)

Fellows_data_top10 = Fellows_data_sub[["Publication_year", "top10_scxw0"]]
Fellows_data_top1 = Fellows_data_sub[["Publication_year", "top1_scxw0"]]

# print(Fellows_data_top1.info())

Fellows_top10_data = (
    Fellows_data_top10.groupby(["Publication_year"]).mean().reset_index()
)

Fellows_top10_data["Percentage"] = Fellows_top10_data["top10_scxw0"] * 100

Fellows_top1_data = Fellows_data_top1.groupby(["Publication_year"]).mean().reset_index()

Fellows_top1_data["Percentage"] = Fellows_top1_data["top1_scxw0"] * 100


### Affiliates data prep

Affiliates_data = pd.read_excel(
    "Data/SciLifeLab-byaddress-20210512.xlsx",
    sheet_name="publ_info",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Affiliates_data_sub = Affiliates_data[
    (Affiliates_data["Publication_year"] > 2012)
    & (Affiliates_data["Publication_year"] < 2019)
]

Affiliates_data_sub = Affiliates_data_sub[
    Affiliates_data_sub["top10_scxw0"].str.contains("None") == False
]

Affiliates_data_sub["top10_scxw0"] = Affiliates_data_sub["top10_scxw0"].astype(float)
Affiliates_data_sub["top1_scxw0"] = Affiliates_data_sub["top1_scxw0"].astype(float)

Affiliates_data_top10 = Affiliates_data_sub[["Publication_year", "top10_scxw0"]]
Affiliates_data_top1 = Affiliates_data_sub[["Publication_year", "top1_scxw0"]]

Affiliates_top10_data = (
    Affiliates_data_top10.groupby(["Publication_year"]).mean().reset_index()
)

Affiliates_top10_data["Percentage"] = Affiliates_top10_data["top10_scxw0"] * 100


Affiliates_top1_data = (
    Affiliates_data_top1.groupby(["Publication_year"]).mean().reset_index()
)

Affiliates_top1_data["Percentage"] = Affiliates_top1_data["top1_scxw0"] * 100

## Facilities data prep

Facilities_data = pd.read_excel(
    "Data/SciLifeLab-facilities-20210512.xlsx",
    sheet_name="publ_data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


Facilities_data_sub = Facilities_data[
    (Facilities_data["Publication_year"] > 2012)
    & (Facilities_data["Publication_year"] < 2019)
]

Facilities_data_sub = Facilities_data_sub[
    Facilities_data_sub["top10_scxw0"].str.contains("None") == False
]

Facilities_data_sub["top10_scxw0"] = Facilities_data_sub["top10_scxw0"].astype(float)
Facilities_data_sub["top1_scxw0"] = Facilities_data_sub["top1_scxw0"].astype(float)

Facilities_data_top10 = Facilities_data_sub[["Publication_year", "top10_scxw0"]]
Facilities_data_top1 = Facilities_data_sub[["Publication_year", "top1_scxw0"]]

Facilities_top10_data = (
    Facilities_data_top10.groupby(["Publication_year"]).mean().reset_index()
)

Facilities_top10_data["Percentage"] = Facilities_top10_data["top10_scxw0"] * 100

Facilities_top1_data = (
    Facilities_data_top1.groupby(["Publication_year"]).mean().reset_index()
)

Facilities_top1_data["Percentage"] = Facilities_top1_data["top1_scxw0"] * 100


## Create graph functions (fellows has one less year, so easiest to do one for that)


def PPtop10_graph_func_facoraff(input, pub_group):
    PPtop10 = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=PPtop10.Publication_year,
            y=PPtop10.Percentage,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=26),
        margin=dict(r=250, t=0, b=0, l=0),
        width=1800,
        height=1000,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = PPtop10["Publication_year"].unique().astype(str)
    Years_int = PPtop10["Publication_year"].unique()
    # modify x-axis
    # add more years as needed
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
            # "<b>" + Years[6] + "</b>",
            # "<b>" + Years[7] + "</b>",
            #           "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            Years[5],
            # Years[6],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(PPtop10["Percentage"])

    if highest_y_value <= 50:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/{}_PPtop10_overyears.svg".format(pub_group))


def PPtop10_graph_func_fell(input, pub_group):
    PPtop10 = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=PPtop10.Publication_year,
            y=PPtop10.Percentage,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=26),
        margin=dict(r=250, t=0, b=0, l=0),
        width=1800,
        height=1000,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = PPtop10["Publication_year"].unique().astype(str)
    Years_int = PPtop10["Publication_year"].unique()
    # modify x-axis
    # add more years as needed
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
            # "<b>" + Years[5] + "</b>",
            # "<b>" + Years[6] + "</b>",
            # "<b>" + Years[7] + "</b>",
            #           "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            # Years[5],
            # Years[6],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(PPtop10["Percentage"])

    if highest_y_value <= 50:
        yaxis_tick = 5
    if highest_y_value > 50:
        yaxis_tick = 10

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/{}_PPtop10_overyears.svg".format(pub_group))


def PPtop1_graph_func_facoraff(input, pub_group):
    PPtop1 = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=PPtop1.Publication_year,
            y=PPtop1.Percentage,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=26),
        margin=dict(r=250, t=0, b=0, l=0),
        width=1800,
        height=1000,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = PPtop1["Publication_year"].unique().astype(str)
    Years_int = PPtop1["Publication_year"].unique()
    # modify x-axis
    # add more years as needed
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
            # "<b>" + Years[6] + "</b>",
            # "<b>" + Years[7] + "</b>",
            #           "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            Years[5],
            # Years[6],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(PPtop1["Percentage"])

    if highest_y_value <= 10:
        yaxis_tick = 1
    if highest_y_value <= 1:
        yaxis_tick = 0.1

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/{}_PPtop1_overyears.svg".format(pub_group))


def PPtop1_graph_func_fell(input, pub_group):
    PPtop1 = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=PPtop1.Publication_year,
            y=PPtop1.Percentage,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=26),
        margin=dict(r=250, t=0, b=0, l=0),
        width=1800,
        height=1000,
        showlegend=False,
    )
    # List years to use in x-axis
    Years = PPtop1["Publication_year"].unique().astype(str)
    Years_int = PPtop1["Publication_year"].unique()
    # modify x-axis
    # add more years as needed
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
            # "<b>" + Years[5] + "</b>",
            # "<b>" + Years[6] + "</b>",
            # "<b>" + Years[7] + "</b>",
            #           "<b>" + Years[8] + "</b>",
        ],
        tickvals=[
            Years[0],
            Years[1],
            Years[2],
            Years[3],
            Years[4],
            # Years[5],
            # Years[6],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(PPtop1["Percentage"])

    if highest_y_value <= 10:
        yaxis_tick = 1
    if highest_y_value <= 1:
        yaxis_tick = 0.1

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/{}_PPtop1_overyears.svg".format(pub_group))


# make plots by applying function
# change svg to other format in functions if needed (sometimes easier to look at them as png)

PPtop10_graph_func_facoraff(Affiliates_top10_data, "Affiliates")
PPtop10_graph_func_facoraff(Facilities_top10_data, "Facilities")
PPtop10_graph_func_fell(Fellows_top10_data, "Fellows")
PPtop1_graph_func_facoraff(Affiliates_top1_data, "Affiliates")
PPtop1_graph_func_facoraff(Facilities_top1_data, "Facilities")
PPtop1_graph_func_fell(Fellows_top1_data, "Fellows")
