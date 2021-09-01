import pandas as pd
import plotly.graph_objects as go
import os

# Fellows data prep

Fellows_data = pd.read_excel(
    "Data/Citations-by-year.xlsx",
    sheet_name="Fellows",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Fellows_data_sub = Fellows_data[
#     (Fellows_data["Publication_year"] > 2013)
#     & (Fellows_data["Publication_year"] < 2021)
# ]

# Look at 2014 for fellows as program starts
Fellows_data_sub = Fellows_data[
    [
        "citations_self_excl_2014",
        "citations_self_excl_2015",
        "citations_self_excl_2016",
        "citations_self_excl_2017",
        "citations_self_excl_2018",
        "citations_self_excl_2019",
        "citations_self_excl_2020",
    ]
]


Fellows_data_sum = Fellows_data_sub.sum(axis=0, skipna=True)

Fellows_data_group = Fellows_data_sum.to_frame(
    name="sum_val",
)
Fellows_data_group["Citation_Year"] = Fellows_data_group.index
Fellows_data_group.reset_index(drop=True, inplace=True)
# print(Fellows_data_group)


# Affiliates data prep

Affiliates_data = pd.read_excel(
    "Data/Citations-by-year.xlsx",
    sheet_name="Byaddress",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# Look at 2013 for Affiliates as SciLifeLab remit changed
Affiliates_data_sub = Affiliates_data[
    [
        "citations_self_excl_2013",
        "citations_self_excl_2014",
        "citations_self_excl_2015",
        "citations_self_excl_2016",
        "citations_self_excl_2017",
        "citations_self_excl_2018",
        "citations_self_excl_2019",
        "citations_self_excl_2020",
    ]
]


Affiliates_data_sum = Affiliates_data_sub.sum(axis=0, skipna=True)

Affiliates_data_group = Affiliates_data_sum.to_frame(
    name="sum_val",
)
Affiliates_data_group["Citation_Year"] = Affiliates_data_group.index
Affiliates_data_group.reset_index(drop=True, inplace=True)
# print(Affiliates_data_group)


# Units/Facilities data prep

Facilities_data = pd.read_excel(
    "Data/Citations-by-year.xlsx",
    sheet_name="Facilities",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# Look at 2013 for Facilities as SciLifeLab remit changed
Facilities_data_sub = Facilities_data[
    [
        "citations_self_excl_2013",
        "citations_self_excl_2014",
        "citations_self_excl_2015",
        "citations_self_excl_2016",
        "citations_self_excl_2017",
        "citations_self_excl_2018",
        "citations_self_excl_2019",
        "citations_self_excl_2020",
    ]
]


Facilities_data_sum = Facilities_data_sub.sum(axis=0, skipna=True)

Facilities_data_group = Facilities_data_sum.to_frame(
    name="sum_val",
)
Facilities_data_group["Citation_Year"] = Facilities_data_group.index
Facilities_data_group.reset_index(drop=True, inplace=True)

# Create graph functions


def Citation_graph_func_facoraff(input, pub_group):
    Citation = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=Citation.Citation_Year,
            y=Citation.sum_val,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=75),
        margin=dict(r=250, t=0, b=0, l=0),
        width=2500,
        height=1700,
        showlegend=False,
    )
    # add more years as needed
    Citation_year = Citation["Citation_Year"].unique()
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        # add more years as needed
        ticktext=[
            "<b>2013</b>",
            "<b>2014</b>",
            "<b>2015</b>",
            "<b>2016</b>",
            "<b>2017</b>",
            "<b>2018</b>",
            "<b>2019</b>",
            "<b>2020</b>",
        ],
        tickvals=[
            Citation_year[0],
            Citation_year[1],
            Citation_year[2],
            Citation_year[3],
            Citation_year[4],
            Citation_year[5],
            Citation_year[6],
            Citation_year[7],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(Citation["sum_val"])

    if highest_y_value > 50000:
        yaxis_tick = 10000
    if highest_y_value > 20000:
        yaxis_tick = 5000
    if highest_y_value <= 10000:
        yaxis_tick = 1000

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    if not os.path.isdir("Plots/largerfonts/"):
        os.mkdir("Plots/largerfonts/")
    # fig.show()
    fig.write_image("Plots/largerfonts/{}_Citation_eachyear.png".format(pub_group))
    fig.write_image("Plots/largerfonts/{}_Citation_eachyear.svg".format(pub_group))


def Citation_graph_func_fell(input, pub_group):
    Citation = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=Citation.Citation_Year,
            y=Citation.sum_val,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=75),
        margin=dict(r=250, t=0, b=0, l=0),
        width=2500,
        height=1700,
        showlegend=False,
    )
    # add more years as needed
    Citation_year = Citation["Citation_Year"].unique()
    fig.update_xaxes(
        title=" ",
        showgrid=True,
        linecolor="black",
        # add more years as needed
        ticktext=[
            "<b>2014</b>",
            "<b>2015</b>",
            "<b>2016</b>",
            "<b>2017</b>",
            "<b>2018</b>",
            "<b>2019</b>",
            "<b>2020</b>",
        ],
        tickvals=[
            Citation_year[0],
            Citation_year[1],
            Citation_year[2],
            Citation_year[3],
            Citation_year[4],
            Citation_year[5],
            Citation_year[6],
            # Citation_year[7],
            # Years[7],
            #            Years[8],
        ],
    )

    highest_y_value = max(Citation["sum_val"])

    if highest_y_value > 50000:
        yaxis_tick = 10000
    if highest_y_value > 20000:
        yaxis_tick = 5000
    if highest_y_value <= 10000:
        yaxis_tick = 1000

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
    fig.write_image("Plots/{}_Citation_eachyear.png".format(pub_group))
    fig.write_image("Plots/{}_Citation_eachyear.svg".format(pub_group))


Citation_graph_func_facoraff(Affiliates_data_group, "Affiliates")
Citation_graph_func_facoraff(Facilities_data_group, "Facilities")
Citation_graph_func_fell(Fellows_data_group, "Fellows")
