"""script to make scatterplot of IEC university scores for units"""
import pandas as pd
import numpy as np
import os
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

All_data = pd.read_excel(
    "Data/IEC University Plot.xlsx",
    sheet_name="All",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Age_data = pd.read_excel(
    "Data/IEC University Plot.xlsx",
    sheet_name="Facility Age",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

IEC_data = pd.merge(Age_data, All_data, how="left", on="No.")

IEC_data = IEC_data[
    ["No.", "Grade IEC_x", "Grade Univ_x", "SciLifeLab Facility since", "Unit_x"]
]

IEC_data.rename(
    columns={
        "No.": "Infra_ref",
        "Grade IEC_x": "IEC_grade",
        "Grade Univ_x": "Uni_grade",
        "SciLifeLab Facility since": "Fac_since",
        "Unit_x": "Name",
    },
    inplace=True,
)

IEC_data.drop_duplicates(subset="Infra_ref", keep="first", inplace=True)
IEC_data = IEC_data.drop([11, 12])
# print(IEC_data.info())
textsize = 20
colours = [
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[17],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[2],
    SCILIFE_COLOURS[15],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[9],
    SCILIFE_COLOURS[16],
]


fig = px.scatter(
    IEC_data,
    x="Uni_grade",
    y="IEC_grade",
    color="Fac_since",
    color_discrete_sequence=colours,
    # text="Name",
)
# fig.update_traces(textposition="top right")
fig.update_traces(
    marker=dict(size=20, line=dict(width=2, color="black")), cliponaxis=False
)

fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=26),
    margin=dict(r=0, t=0, b=0, l=0),
    width=2500,
    height=1500,
    showlegend=True,
    legend=dict(
        title="SciLifeLab Facility Since:    ",
        orientation="h",
        yanchor="bottom",
        y=1,
        xanchor="right",
        x=1,
    ),
)

# modify x-axis
fig.update_xaxes(
    title="<br>University Mean Grade",
    showgrid=True,
    linecolor="black",
)

# max_pubs = max(pubs_fund_data["log_Count"])

# modify y-axis
fig.update_yaxes(
    title="IEC Grade<br>",  # keep the break to give y-axis title space between graph
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    # range=[0, max_pubs * 1.15],
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[0],
        y=IEC_data.IEC_grade[0],
        ax=0,
        ay=-70,
        showarrow=True,
        text=IEC_data.Name[0],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[1],
        y=IEC_data.IEC_grade[1],
        ax=0,
        ay=120,
        showarrow=True,
        text=IEC_data.Name[1],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[2],
        y=IEC_data.IEC_grade[2],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[2],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[3],
        y=IEC_data.IEC_grade[3],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[3],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[4],
        y=IEC_data.IEC_grade[4],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[4],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[5],
        y=IEC_data.IEC_grade[5],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[5],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[6],
        y=IEC_data.IEC_grade[6],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[6],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[7],
        y=IEC_data.IEC_grade[7],
        ax=0,
        ay=70,
        showarrow=True,
        text=IEC_data.Name[7],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[8],
        y=IEC_data.IEC_grade[8],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[8],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[9],
        y=IEC_data.IEC_grade[9],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[9],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[10],
        y=IEC_data.IEC_grade[10],
        ax=0,
        ay=30,
        showarrow=True,
        text=IEC_data.Name[10],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[13],
        y=IEC_data.IEC_grade[13],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[13],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[14],
        y=IEC_data.IEC_grade[14],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[14],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[15],
        y=IEC_data.IEC_grade[15],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[15],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[16],
        y=IEC_data.IEC_grade[16],
        ax=0,
        ay=90,
        showarrow=True,
        text=IEC_data.Name[16],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[17],
        y=IEC_data.IEC_grade[17],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[17],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[18],
        y=IEC_data.IEC_grade[18],
        ax=0,
        ay=-150,
        showarrow=True,
        text=IEC_data.Name[18],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[21],
        y=IEC_data.IEC_grade[21],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[21],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[22],
        y=IEC_data.IEC_grade[22],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[22],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[23],
        y=IEC_data.IEC_grade[23],
        ax=0,
        ay=120,
        showarrow=True,
        text=IEC_data.Name[23],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[24],
        y=IEC_data.IEC_grade[24],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[24],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[25],
        y=IEC_data.IEC_grade[25],
        ax=0,
        ay=-100,
        showarrow=True,
        text=IEC_data.Name[25],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[26],
        y=IEC_data.IEC_grade[26],
        ax=0,
        ay=-30,
        showarrow=True,
        text=IEC_data.Name[26],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[27],
        y=IEC_data.IEC_grade[27],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[27],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[31],
        y=IEC_data.IEC_grade[31],
        ax=0,
        ay=-70,
        showarrow=True,
        text=IEC_data.Name[31],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[32],
        y=IEC_data.IEC_grade[32],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[32],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[33],
        y=IEC_data.IEC_grade[33],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[33],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[34],
        y=IEC_data.IEC_grade[34],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[34],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[35],
        y=IEC_data.IEC_grade[35],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[35],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[36],
        y=IEC_data.IEC_grade[36],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[36],
    )
)


fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[39],
        y=IEC_data.IEC_grade[39],
        ax=0,
        ay=120,
        showarrow=True,
        arrowcolor="white",
        text="and " + IEC_data.Name[39],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[37],
        y=IEC_data.IEC_grade[37],
        ax=0,
        ay=100,
        showarrow=True,
        text=IEC_data.Name[37],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[38],
        y=IEC_data.IEC_grade[38],
        ax=0,
        ay=50,
        showarrow=True,
        text=IEC_data.Name[38],
    )
)

fig.add_annotation(
    dict(
        font=dict(color="black", size=textsize),
        x=IEC_data.Uni_grade[40],
        y=IEC_data.IEC_grade[40],
        ax=0,
        ay=-50,
        showarrow=True,
        text=IEC_data.Name[40],
    )
)

if not os.path.isdir("Plots"):
    os.mkdir("Plots")

# fig.show()
fig.write_image("Plots/IEC_scores_labels.svg", scale=3)
