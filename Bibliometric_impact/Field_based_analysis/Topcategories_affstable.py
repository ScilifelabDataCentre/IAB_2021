""" script to show top 20 subject (proportion of papers on PPtop10) - overall"""

import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

trend_data_aff = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_byaddress-2.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_byaddres",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

trend_data_aff_sub = trend_data_aff[
    (trend_data_aff["Publication_year"] > 2014)
    & (trend_data_aff["Publication_year"] < 2019)
]

trend_data_aff_sub = trend_data_aff_sub[
    (trend_data_aff_sub["Doc_type_code_rev"] == "RV")
    | (trend_data_aff_sub["Doc_type_code_rev"] == "AR")
    | (trend_data_aff_sub["Doc_type_code_rev"] == "PP")
]

trend_group = (
    trend_data_aff_sub.groupby(["Subject_category"])
    .agg(field_count=("Subject_category", "size"), pptop10=("Top10_scxwo", "mean"))
    .reset_index()
)

# print(trend_group)
# calculate actual papers in each year
total_papers = len(trend_data_aff_sub.drop_duplicates(subset="UT", keep="first"))
trend_group["tot_papers"] = total_papers
# subject_group = (
#     total_papers.groupby(["Subject_category"])
#     .agg(tot_year=("Subject_category", "size"))
#     .reset_index()
# )

# print(year_group)

# getprops = pd.merge(
#     trend_group,
#     subject_group,
#     how="left",
#     on="Subject_category",
# )

trend_group["No_papers"] = trend_group["field_count"]
trend_group.sort_values(by="No_papers", ascending=False, inplace=True)
trend_group["pptop10"] = trend_group["pptop10"] * 100
trend_group = trend_group[trend_group["No_papers"] >= 100]
trend_group.drop(["field_count", "tot_papers"], axis=1, inplace=True)
trend_group["Subject_category"] = trend_group["Subject_category"].replace(
    "CHEMISTRY, MULTIDISCIPLINARY",
    "CHEMISTRY (MULTIDISCIPLINARY)",
)
# trend_group = trend_group.head(20)
# trend_group = trend_group.round(2)
print(trend_group)
fig3 = go.Figure(
    data=[
        go.Table(
            columnwidth=[20, 10, 10],
            header=dict(
                values=[
                    "<b>Subject Category</b>",
                    "<b>PP(top10)</b>",
                    "<b>Number of Publications</b>",
                ],
                align=["left", "center", "center"],
                fill_color=SCILIFE_COLOURS[0],
                font=dict(color="black", size=14),
                line=dict(width=0),
            ),
            cells=dict(
                values=(
                    trend_group["Subject_category"],
                    trend_group["pptop10"],
                    trend_group["No_papers"],
                ),
                align=["left", "center", "center"],
                format=[[None], [".0f"], [None]],
                fill_color=[[SCILIFE_COLOURS[1], "white"] * 10],
                font=dict(color="black", size=12),
                height=30,
                line=dict(width=0),
            ),
        )
    ]
)
# fig3.show()
fig3.update_layout(autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=450)
fig3.write_image("Plots/UPDATE1518/summary_table_affs_arttypes.png")
fig3.write_image("Plots/UPDATE1518/summary_table_affs_arttypes.svg")
trend_group.to_excel("Plots/UPDATE1518/summary_table_affs_arttypes_data.xlsx")
