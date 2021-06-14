"""Make matrix/bubble plot showing how facilities work in top 6 subject categories"""
import pandas as pd
import numpy as np
import os

# from collections import Counter
import plotly.graph_objects as go
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)
from facilities_and_fields_top3table import (
    Facs_fieldandunit,
    facilities_list,
    facilities_official,
)

# Facs_fieldandunit has data on subject categories (fields) and units (formerly facilities)

# filter years of interest
Facs_fieldandunit_sub = Facs_fieldandunit[
    (Facs_fieldandunit["Publication_year"] > 2012)
    & (Facs_fieldandunit["Publication_year"] < 2021)
]

# filter to include only 6 'top' subject categories (fields of work)
Facs_fieldandunit_sub = Facs_fieldandunit_sub[
    (Facs_fieldandunit_sub["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")
    | (Facs_fieldandunit_sub["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")
    | (
        Facs_fieldandunit_sub["Subject_category"]
        == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY"
    )
    | (Facs_fieldandunit_sub["Subject_category"] == "ONCOLOGY")
    | (Facs_fieldandunit_sub["Subject_category"] == "CELL BIOLOGY")
    | (Facs_fieldandunit_sub["Subject_category"] == "GENETICS & HEREDITY")
]


Facs_fieldandunit_sub = Facs_fieldandunit_sub[["Subject_category", "Labels"]]

values = Facs_fieldandunit_sub[
    Facs_fieldandunit_sub["Labels"].str.contains(facilities_list[0])
]
values = (
    values.groupby("Subject_category")
    .agg(Count=("Labels", "count"))
    .reset_index()
    .sort_values(by="Count", ascending=False)
)
values["Unit"] = facilities_official[0]
df = values

for i in range(1, 29):
    values = Facs_fieldandunit_sub[
        Facs_fieldandunit_sub["Labels"].str.contains(facilities_list[i])
    ]
    values = (
        values.groupby("Subject_category")
        .agg(Count=("Labels", "count"))
        .reset_index()
        .sort_values(by="Count", ascending=False)
    )
    values["Unit"] = facilities_official[i]
    df = pd.concat([df, values])
# print(df)
df["Count_scaled"] = df["Count"] * 100

colours = [
    SCILIFE_COLOURS[14],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[18],
    SCILIFE_COLOURS[8],
] * 100

biochemres = df[(df["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")]
oncology = df[(df["Subject_category"] == "ONCOLOGY")]
biotechmicro = df[(df["Subject_category"] == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY")]
cellbio = df[(df["Subject_category"] == "CELL BIOLOGY")]
biochemmolec = df[(df["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")]
genetics = df[(df["Subject_category"] == "GENETICS & HEREDITY")]


fig = go.Figure(
    data=[
        go.Scatter(
            x=biochemres.Unit,
            y=biochemres.Subject_category,
            mode="markers",
            marker=dict(
                size=biochemres.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[0],
            ),
        ),
        go.Scatter(
            x=oncology.Unit,
            y=oncology.Subject_category,
            mode="markers",
            marker=dict(
                size=oncology.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[1],
            ),
        ),
        go.Scatter(
            x=biotechmicro.Unit,
            y=biotechmicro.Subject_category,
            mode="markers",
            marker=dict(
                size=biotechmicro.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[2],
            ),
        ),
        go.Scatter(
            x=cellbio.Unit,
            y=cellbio.Subject_category,
            mode="markers",
            marker=dict(
                size=cellbio.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[3],
            ),
        ),
        go.Scatter(
            x=biochemmolec.Unit,
            y=biochemmolec.Subject_category,
            mode="markers",
            marker=dict(
                size=biochemmolec.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[4],
            ),
        ),
        go.Scatter(
            x=genetics.Unit,
            y=genetics.Subject_category,
            mode="markers",
            marker=dict(
                size=genetics.Count_scaled,
                sizemode="area",
                sizeref=2.0 * max(df.Count_scaled) / (40.0 ** 2),
                sizemin=4,
                color=colours[5],
            ),
        ),
    ]
)


fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=18),
    margin=dict(r=0, t=0, b=0, l=0),
    width=2500,
    height=800,
    showlegend=False,
)

# modify x-axis
fig.update_xaxes(
    title=" ",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
)


# modify y-axis
fig.update_yaxes(
    title=" ",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    ticktext=[
        "Genetics & Heredity",
        "Biochemistry & Molecular Biology",
        "Cell Biology",
        "Biotechnology & Applied Microbiology",
        "Oncology",
        "Biochemical Research Methods",
    ],
    tickvals=[
        "GENETICS & HEREDITY",
        "BIOCHEMISTRY & MOLECULAR BIOLOGY",
        "CELL BIOLOGY",
        "BIOTECHNOLOGY & APPLIED MICROBIOLOGY",
        "ONCOLOGY",
        "BIOCHEMICAL RESEARCH METHODS",
    ],
)

# fig.show()
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
fig.write_image("Plots/Bubbleplot_facstop6fields.png")
fig.write_image("Plots/Bubbleplot_facstop6fields.svg")
