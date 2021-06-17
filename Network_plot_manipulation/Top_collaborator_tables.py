import csv
import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

VOS_collab = pd.read_csv(
    "Data/over20copubsmap_edited.txt",
    sep="\t",
    #    engine="c",
)
# Above is our list of national collaborators post string-processing
# Need two top 10 tables - one with ranking based on MNCS and one with ranking based on Document number

VOS_collab.rename(
    columns={
        "label": "Name",
        "weight<Total link strength>": "Links",
        "weight<Documents>": "Docs",
        "score<Avg. citations>": "MNCS",
    },
    inplace=True,
)

topdocs = VOS_collab[["Name", "Links", "Docs"]]
topdocs.sort_values(by="Docs", ascending=False, inplace=True)
topdocs = topdocs[~topdocs["Name"].str.contains("SciLifeLab")]
topdocs = topdocs.head(20)

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
                    topdocs["Name"],
                    topdocs["Docs"],
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
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=640
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_docs.write_image("Plots/toptwenty_collabs_docs.png")
fig_docs.write_image("Plots/toptwenty_collabs_docs.svg")

# Get just international collabs

topdocs = VOS_collab[["Name", "Links", "Docs"]]
topdocs.sort_values(by="Docs", ascending=False, inplace=True)

intdocs = topdocs[~topdocs["Name"].str.contains("SciLifeLab")]
intdocs = intdocs[~intdocs["Name"].str.contains("Uppsala University")]
intdocs = intdocs[~intdocs["Name"].str.contains("Karolinska Institute")]
intdocs = intdocs[~intdocs["Name"].str.contains("KTH Royal Institute of Technology")]
intdocs = intdocs[~intdocs["Name"].str.contains("Stockholm University")]
intdocs = intdocs[~intdocs["Name"].str.contains("Karolinska University Hospital")]
intdocs = intdocs[~intdocs["Name"].str.contains("Lund University")]
intdocs = intdocs[
    ~intdocs["Name"].str.contains("Swedish University of Agricultural Sciences")
]

intdocs = intdocs[~intdocs["Name"].str.contains("University of Gothenburg")]
intdocs = intdocs[~intdocs["Name"].str.contains("Chalmers University of Technology")]
intdocs = intdocs[~intdocs["Name"].str.contains("Umeå University")]
intdocs = intdocs[~intdocs["Name"].str.contains("Skåne University Hospital")]
intdocs = intdocs[~intdocs["Name"].str.contains("Sahlgrenska University Hospital")]
intdocs = intdocs[~intdocs["Name"].str.contains("Linköping University")]
intdocs = intdocs[~intdocs["Name"].str.contains("Dalarna University College")]
intdocs = intdocs[~intdocs["Name"].str.contains("Örebro University")]
topdocs = intdocs
topdocs = topdocs.head(20)


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
                    topdocs["Name"],
                    topdocs["Docs"],
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
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=640
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_docs.write_image("Plots/toptwenty_int_collabs_docs.png")
fig_docs.write_image("Plots/toptwenty_int_collabs_docs.svg")

# Need to make MNCS plots

topmncs = VOS_collab[["Name", "Links", "MNCS"]]
topmncs.sort_values(by="MNCS", ascending=False, inplace=True)

topmncs = topmncs[~topmncs["Name"].str.contains("SciLifeLab")]
topmncs = topmncs.head(20)
topmncs = topmncs.round(2)
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
                    topmncs["Name"],
                    topmncs["MNCS"],
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
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=630
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_mncs.write_image("Plots/toptwenty_collabs_mncs.png")
fig_mncs.write_image("Plots/toptwenty_collabs_mncs.svg")

# Get just international collabs

topmncs = VOS_collab[["Name", "Links", "MNCS"]]
topmncs.sort_values(by="MNCS", ascending=False, inplace=True)

intmncs = topmncs[~topmncs["Name"].str.contains("SciLifeLab")]
intmncs = intmncs[~intmncs["Name"].str.contains("Uppsala University")]
intmncs = intmncs[~intmncs["Name"].str.contains("Karolinska Institute")]
intmncs = intmncs[~intmncs["Name"].str.contains("KTH Royal Institute of Technology")]
intmncs = intmncs[~intmncs["Name"].str.contains("Stockholm University")]
intmncs = intmncs[~intmncs["Name"].str.contains("Karolinska University Hospital")]
intmncs = intmncs[~intmncs["Name"].str.contains("Lund University")]
intmncs = intmncs[
    ~intmncs["Name"].str.contains("Swedish University of Agricultural Sciences")
]

intmncs = intmncs[~intmncs["Name"].str.contains("University of Gothenburg")]
intmncs = intmncs[~intmncs["Name"].str.contains("Chalmers University of Technology")]
intmncs = intmncs[~intmncs["Name"].str.contains("Umeå University")]
intmncs = intmncs[~intmncs["Name"].str.contains("Skåne University Hospital")]
intmncs = intmncs[~intmncs["Name"].str.contains("Sahlgrenska University Hospital")]
intmncs = intmncs[~intmncs["Name"].str.contains("Linköping University")]
intmncs = intmncs[~intmncs["Name"].str.contains("Dalarna University College")]
intmncs = intmncs[~intmncs["Name"].str.contains("Örebro University")]
topmncs = intmncs
topmncs = topmncs.head(20)
topmncs = topmncs.round(2)

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
                    topmncs["Name"],
                    topmncs["MNCS"],
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
    autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=630
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
fig_mncs.write_image("Plots/toptwenty_int_collabs_mncs.png")
fig_mncs.write_image("Plots/toptwenty_int_collabs_mncs.svg")
