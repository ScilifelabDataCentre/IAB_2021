"""This script will produce pie charts showing the proportion of infra papers labelled with service/tech/collab"""


import pandas as pd
import plotly.graph_objects as go
import os
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

# # first do pie chart for all infra

# allinfra = pd.read_excel(
#     "Data/infra_raw_numbers_tocheck_5CATEGORIES.xlsx",
#     sheet_name="Sheet1",
#     header=0,
#     engine="openpyxl",
#     keep_default_na=False,
# )

# allinfra = (
#     allinfra.groupby(["Qualifiers"]).agg(No_papers=("Qualifiers", "size")).reset_index()
# )

# allinfra["Percentage"] = (
#     (allinfra["No_papers"] / sum(allinfra["No_papers"])) * 100
# ).round(1)

# colours = [
#     SCILIFE_COLOURS[0],
#     SCILIFE_COLOURS[4],
#     SCILIFE_COLOURS[12],
#     SCILIFE_COLOURS[8],
#     SCILIFE_COLOURS[16],
# ]

# # Edited this to fit more nicely
# allinfra["Qualifiers"] = allinfra["Qualifiers"].replace(
#     "Technology development",
#     "Technology<br>development",
# )
# print(allinfra)
# fig = go.Figure(
#     go.Pie(
#         values=allinfra["Percentage"],
#         labels=allinfra["Qualifiers"],
#         hole=0.6,
#         marker=dict(colors=colours, line=dict(color="#000000", width=1)),
#         direction="clockwise",
#         sort=True,
#     )
# )

# fig.update_traces(
#     textposition="outside",
#     texttemplate="%{label} <br>(%{value}%)",
# )
# fig.update_layout(
#     margin=dict(l=0, r=0, b=0, t=0),
#     font=dict(size=23),
#     showlegend=False,
#     width=1000,
#     height=1000,
#     autosize=False,
# )
# if not os.path.isdir("Plots"):
#     os.mkdir("Plots")
# # fig.show()

# fig.write_image("Plots/allinfralabels_pie_updatelabs.svg", scale=3)
# fig.write_image("Plots/allinfralabels_pie_updatelabs.png", scale=3)

# # Now for the papers interacting

# interinf = pd.read_excel(
#     "Data/unique_qualifier_labels_5CATEGORIES.xlsx",
#     sheet_name="Sheet1",
#     header=0,
#     engine="openpyxl",
#     keep_default_na=False,
# )

# interinf = (
#     interinf.groupby(["Qualifiers"]).agg(No_papers=("Qualifiers", "size")).reset_index()
# )

# interinf["Percentage"] = (
#     (interinf["No_papers"] / sum(interinf["No_papers"])) * 100
# ).round(1)

# print(interinf)
# colours = [
#     SCILIFE_COLOURS[0],
#     SCILIFE_COLOURS[4],
#     SCILIFE_COLOURS[12],
#     SCILIFE_COLOURS[8],
#     SCILIFE_COLOURS[16],
# ]

# # Edited this to fit more nicely
# interinf["Qualifiers"] = interinf["Qualifiers"].replace(
#     "Technology development",
#     "Technology<br>development",
# )


# fig = go.Figure(
#     go.Pie(
#         values=interinf["Percentage"],
#         labels=interinf["Qualifiers"],
#         hole=0.6,
#         marker=dict(colors=colours, line=dict(color="#000000", width=1)),
#         direction="clockwise",
#         sort=True,
#     )
# )

# fig.update_traces(
#     textposition="outside",
#     texttemplate="%{label} <br>(%{value}%)",
# )
# fig.update_layout(
#     margin=dict(l=0, r=0, b=0, t=0),
#     font=dict(size=23),
#     showlegend=False,
#     width=1000,
#     height=1000,
#     autosize=False,
# )
# if not os.path.isdir("Plots"):
#     os.mkdir("Plots")
# # fig.show()

# fig.write_image("Plots/interinfralabels_pie_updatelabs.svg", scale=3)
# fig.write_image("Plots/interinfralabels_pie_updatelabs.png", scale=3)

# Now for the papers interacting just 2019-20

interinf1920 = pd.read_excel(
    "Data/unique_qualifier_labels_1920_5CATEGORIES.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

interinf1920 = (
    interinf1920.groupby(["Qualifiers"])
    .agg(No_papers=("Qualifiers", "size"))
    .reset_index()
)

interinf1920["Percentage"] = (
    (interinf1920["No_papers"] / sum(interinf1920["No_papers"])) * 100
).round(1)

print(interinf1920)
colours = [
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[16],
]

# Edited this to fit more nicely
interinf1920["Qualifiers"] = interinf1920["Qualifiers"].replace(
    "Technology development",
    "Technology<br>development",
)


fig = go.Figure(
    go.Pie(
        values=interinf1920["Percentage"],
        labels=interinf1920["Qualifiers"],
        hole=0.6,
        marker=dict(colors=colours, line=dict(color="#000000", width=1)),
        direction="clockwise",
        sort=True,
    )
)

fig.update_traces(
    textposition="outside",
    texttemplate="%{label} <br>(%{value}%)",
)
fig.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    font=dict(size=23),
    showlegend=False,
    width=1000,
    height=1000,
    autosize=False,
)
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
# fig.show()

fig.write_image("Plots/interinfralabels_pie_updatelabs1920.svg", scale=3)
fig.write_image("Plots/interinfralabels_pie_updatelabs1920.png", scale=3)
