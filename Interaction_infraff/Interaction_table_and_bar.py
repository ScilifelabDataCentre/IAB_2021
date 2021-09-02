import pandas as pd
import os
import plotly.graph_objects as go
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

# facilities_pub = pd.read_excel(
#     "Data/Facilities_20210419.xlsx", sheet_name="Sheet1", engine="openpyxl"
# )
facilities_bib = pd.read_excel(
    "Data/SciLifeLab-facilities-20210512.xlsx",
    sheet_name="publ_data",
    engine="openpyxl",
)
affiliates_bib = pd.read_excel(
    "Data/SciLifeLab-byaddress-20210512.xlsx",
    sheet_name="publ_info",
    engine="openpyxl",
)

facs_bib = facilities_bib[
    (facilities_bib["Publication_year"] > 2014)
    & (facilities_bib["Publication_year"] < 2019)
]

affs_bib = affiliates_bib[
    (affiliates_bib["Publication_year"] > 2014)
    & (affiliates_bib["Publication_year"] < 2019)
]

facs_bib = facs_bib[["UT", "DOI", "Doc_type_code_rev", "top10_scxw0"]]
affs_bib = affs_bib[["UT", "DOI", "Doc_type_code_rev", "top10_scxw0"]]


intersect = pd.merge(
    affs_bib,
    facs_bib,
    on=["UT", "Doc_type_code_rev", "top10_scxw0"],
    how="inner",
)

# print(intersect.info())

# intersect now contains all of the overlapping papers 2015-18
# need to be able to break these down by field and by label. This requires matching to two files
# the raw publications database information (use DOI), and the document with fields in (use UT)

# the fields data from KTH
subject_categories = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_facilities.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_faciliti",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

intersect_subcat = intersect[["UT", "Doc_type_code_rev"]]

# get columns of interest
subject_categories = subject_categories[
    ["UT", "Doc_type_code_rev", "Top10_scxwo", "Subject_category"]
]

# rename columns as needed to match
subject_categories.rename(columns={"Top10_scxwo": "PPtop10score_use"}, inplace=True)

# print(intersect_subcat.info())
# print(subject_categories.info())

intersect_subjects = pd.merge(
    intersect_subcat,
    subject_categories,
    on=["UT", "Doc_type_code_rev"],
    how="left",
)

# you can check how many unique UTs you have. (you'll have more than you expect, as papers are in multiple categories)
# print(len(intersect_subjects["UT"].unique()))

# Make a table showing the top categories (N), and the impact (PPtop10)

intersect_subjects = intersect_subjects[
    (intersect_subjects["Doc_type_code_rev"] == "RV")
    | (intersect_subjects["Doc_type_code_rev"] == "AR")
    | (intersect_subjects["Doc_type_code_rev"] == "PP")
]

trend_group = (
    intersect_subjects.groupby(["Subject_category"])
    .agg(No_papers=("Subject_category", "size"), pptop10=("PPtop10score_use", "mean"))
    .reset_index()
)

trend_group.sort_values(by="No_papers", ascending=False, inplace=True)
trend_group["pptop10"] = (trend_group["pptop10"] * 100).astype(int)
trend_group = trend_group[trend_group["No_papers"] > 20]

trend_group = trend_group.replace(
    "CHEMISTRY, MEDICINAL",
    "CHEMISTRY (MEDICINAL)",
)
trend_group = trend_group.replace(
    "MEDICINE, RESEARCH & EXPERIMENTAL",
    "MEDICINE (RESEARCH & EXPERIMENTAL)",
)
trend_group = trend_group.replace(
    "CHEMISTRY, ORGANIC",
    "CHEMISTRY (ORGANIC)",
)

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
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
# fig3.show()
fig3.update_layout(autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=600)
fig3.write_image("Plots/summary_table_intersections.png")
fig3.write_image("Plots/summary_table_intersections.svg")
trend_group.to_excel("Plots/summary_table_intersections_data.xlsx")


# raw database extract from publications database - mext time, ideally use an extraction with seperate labels. DB changes prevented here
facilities_label_pub = pd.read_excel(
    "Data/Facilities_20210419.xlsx", sheet_name="Sheet1", engine="openpyxl"
)
facilities_label_pub = facilities_label_pub[["DOI", "Qualifiers"]]

intersect_labels = intersect[["Doc_type_code_rev", "top10_scxw0", "DOI_y"]]
intersect_labels.rename(columns={"DOI_y": "DOI"}, inplace=True)


intersect_infra_labels = pd.merge(
    intersect_labels,
    facilities_label_pub,
    on=["DOI"],
    how="inner",
)


intersect_infra_labels = intersect_infra_labels[
    (intersect_infra_labels["Doc_type_code_rev"] == "RV")
    | (intersect_infra_labels["Doc_type_code_rev"] == "AR")
    | (intersect_infra_labels["Doc_type_code_rev"] == "PP")
]
# print(intersect_infra_labels.info())
# intersect_infra_labels.to_excel("test_labels.xlsx")

unique_labels = pd.read_excel(
    "Data/unique_qualifier_labels.xlsx",
    sheet_name="Sheet1",
    engine="openpyxl",
)

qualifier_labels = (
    unique_labels.groupby(["Qualifiers"])
    .agg(No_papers=("Qualifiers", "size"), pptop10=("top10_scxw0", "mean"))
    .reset_index()
)
qualifier_labels["pptop10"] = (qualifier_labels["pptop10"] * 100).astype(int)

# we didnt use this table, but you could in future years
print(qualifier_labels)
fig4 = go.Figure(
    data=[
        go.Table(
            columnwidth=[20, 10, 10],
            header=dict(
                values=[
                    "<b>Study Type</b>",
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
                    qualifier_labels["Qualifiers"],
                    qualifier_labels["pptop10"],
                    qualifier_labels["No_papers"],
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
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
# fig4.show()
fig4.update_layout(autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=330)
fig4.write_image("Plots/summary_table_studytype_intersections.png")
fig4.write_image("Plots/summary_table_studytype_intersections.svg")
qualifier_labels.to_excel("Plots/summary_table_studytype_intersections_data.xlsx")

# now make them into a plot
qualifier_labels = qualifier_labels.replace(
    "Technology development",
    "Technology<br>development",
)


def bar_studytypes(input, pub_group):
    qualifier_labels = input
    # Make bar chart
    fig = go.Figure(
        go.Bar(
            x=qualifier_labels.Qualifiers,
            y=qualifier_labels.No_papers,
            text=qualifier_labels.pptop10,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        autosize=False,
        font=dict(size=50),
        margin=dict(r=250, t=0, b=0, l=0),
        width=1500,
        height=1000,
        showlegend=False,
    )
    fig.update_xaxes(
        title=" ",
        showgrid=False,
        gridcolor="lightgrey",
        linecolor="black",
    )

    highest_y_value = max(qualifier_labels["No_papers"])

    if highest_y_value <= 50:
        yaxis_tick = 5
    if highest_y_value > 100:
        yaxis_tick = 100

    # modify y-axis
    fig.update_yaxes(
        title=" ",
        showgrid=True,
        gridcolor="lightgrey",
        linecolor="black",
        dtick=yaxis_tick,
        range=[0, float(highest_y_value * 1.15)],
    )
    fig.update_traces(texttemplate="%{text}" + "%", textposition="outside")
    if not os.path.isdir("Plots/"):
        os.mkdir("Plots/")
    # fig.show()
    fig.write_image("Plots/{}_studytype.svg".format(pub_group))
    fig.write_image("Plots/{}_studytype.png".format(pub_group))


bar_studytypes(qualifier_labels, "Intersect")
