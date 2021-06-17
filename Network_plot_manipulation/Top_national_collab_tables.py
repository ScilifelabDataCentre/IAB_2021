import csv
import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

VOS_Swe = pd.read_csv(
    "Data/Justswedishmap_edited.txt",
    sep="\t",
    #    engine="c",
)
# Above is our list of national collaborators post string-processing
# Need two top 10 tables - one with ranking based on MNCS and one with ranking based on Document number

topdocs = VOS_Swe[["label", "weight<Total link strength>", "weight<Documents>"]]
topdocs.sort_values(by="weight<Documents>", ascending=False, inplace=True)
topdocs.rename(
    columns={
        "label": "Name",
        "weight<Total link strength>": "Links",
        "weight<Documents>": "Docs",
    },
    inplace=True,
)
topdocs = topdocs[~topdocs["Name"].str.contains("SciLifeLab")]
toptendocs = topdocs.head(10)

fig_docs = go.Figure(
    data=[
        go.Table(
            columnwidth=[20, 10],
            header=dict(
                values=[
                    "<b>Collaborator name</b>",
                    "<b>Number of Publications</b>",
                ],
                align=["left", "center"],
                fill_color=SCILIFE_COLOURS[0],
                font=dict(color="black", size=14),
                line=dict(width=0),
            ),
            cells=dict(
                values=(
                    toptendocs["Name"],
                    toptendocs["Docs"],
                ),
                align=["left", "center"],
                fill_color=[[SCILIFE_COLOURS[1], "white"] * 10],
                font=dict(color="black", size=12),
                height=30,
                line=dict(width=0),
            ),
        )
    ]
)
# fig_docs.show()
fig_docs.update_layout(
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=330
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_docs.write_image("Plots/topten_national_collabs_docs.png")
fig_docs.write_image("Plots/topten_national_collabs_docs.svg")

# Need to make MNCS plots

topmncs = VOS_Swe[["label", "weight<Total link strength>", "score<Avg. citations>"]]
topmncs.sort_values(by="score<Avg. citations>", ascending=False, inplace=True)
topmncs.rename(
    columns={
        "label": "Name",
        "weight<Total link strength>": "Links",
        "score<Avg. citations>": "MNCS",
    },
    inplace=True,
)

topmncs = topmncs[~topmncs["Name"].str.contains("SciLifeLab")]
toptenmncs = topmncs.head(10)
toptenmncs = toptenmncs.round(2)
fig_mncs = go.Figure(
    data=[
        go.Table(
            columnwidth=[20, 10],
            header=dict(
                values=[
                    "<b>Collaborator name</b>",
                    "<b>MNCS</b>",
                ],
                align=["left", "center"],
                fill_color=SCILIFE_COLOURS[0],
                font=dict(color="black", size=14),
                line=dict(width=0),
            ),
            cells=dict(
                values=(
                    toptenmncs["Name"],
                    toptenmncs["MNCS"],
                ),
                align=["left", "center"],
                fill_color=[[SCILIFE_COLOURS[1], "white"] * 10],
                font=dict(color="black", size=12),
                height=30,
                line=dict(width=0),
            ),
        )
    ]
)
# fig_mncs.show()
fig_mncs.update_layout(
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=330
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_mncs.write_image("Plots/topten_national_collabs_mncs.png")
fig_mncs.write_image("Plots/topten_national_collabs_mncs.svg")
