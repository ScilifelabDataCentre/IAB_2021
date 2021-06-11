"""script to examine how work in 6 key areas of interest change over time"""
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

trend_data_fac = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_facilities.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_faciliti",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

benchmark = pd.read_excel(
    "Data/SciLifeLab_swe_benchmark.xlsx",
    sheet_name="SciLifeLab_swe_benchmark",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

trend_data_fac_sub = trend_data_fac[
    (trend_data_fac["Publication_year"] > 2012)
    & (trend_data_fac["Publication_year"] < 2019)
]
trend_data_fac_sub = trend_data_fac_sub[
    (trend_data_fac_sub["Doc_type_code_rev"] == "RV")
    | (trend_data_fac_sub["Doc_type_code_rev"] == "AR")
    | (trend_data_fac_sub["Doc_type_code_rev"] == "PP")
]

# see how many levels each year
# cats_13 = trend_data_fac[(trend_data_fac["Publication_year"] == 2013)]
# cats_14 = trend_data_fac[(trend_data_fac["Publication_year"] == 2014)]
# cats_15 = trend_data_fac[(trend_data_fac["Publication_year"] == 2015)]
# cats_16 = trend_data_fac[(trend_data_fac["Publication_year"] == 2016)]
# cats_17 = trend_data_fac[(trend_data_fac["Publication_year"] == 2017)]
# cats_18 = trend_data_fac[(trend_data_fac["Publication_year"] == 2018)]
# print(len(cats_13["Subject_category"].unique()))
# print(len(cats_14["Subject_category"].unique()))
# print(len(cats_15["Subject_category"].unique()))
# print(len(cats_16["Subject_category"].unique()))
# print(len(cats_17["Subject_category"].unique()))
# print(len(cats_18["Subject_category"].unique()))

trend_data_fac_sub_field = trend_data_fac_sub[
    (trend_data_fac_sub["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")
    | (trend_data_fac_sub["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")
    | (trend_data_fac_sub["Subject_category"] == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY")
    | (trend_data_fac_sub["Subject_category"] == "ONCOLOGY")
    | (trend_data_fac_sub["Subject_category"] == "CELL BIOLOGY")
    | (trend_data_fac_sub["Subject_category"] == "GENETICS & HEREDITY")
]

trend_group = (
    trend_data_fac_sub_field.groupby(["Publication_year", "Subject_category"])
    .agg(field_count=("Subject_category", "size"), pptop10=("Top10_scxwo", "mean"))
    .reset_index()
)

# print(trend_group)
# calculate actual papers in each year
total_papers = trend_data_fac_sub.drop_duplicates(subset="UT", keep="first")
year_group = (
    total_papers.groupby(["Publication_year"])
    .agg(tot_year=("Publication_year", "size"))
    .reset_index()
)

# print(year_group)

getprops = pd.merge(
    trend_group,
    year_group,
    how="left",
    on="Publication_year",
)

getprops["Prop_papers"] = getprops["field_count"] / getprops["tot_year"]

benchmark_compare = benchmark[
    [
        "Publication_year",
        "Subject_category",
        "Prop_Top10_scxwo_full",
    ]
]

benchmark_compare = benchmark_compare.rename(
    columns={
        "Prop_Top10_scxwo_full": "Full_bench",
    }
)

mergebench = pd.merge(
    getprops,
    benchmark_compare,
    how="left",
    on=["Publication_year", "Subject_category"],
)

mergebench["relative_bench"] = mergebench["Full_bench"] < mergebench["pptop10"]

# if mergebench["Full_bench"] > mergebench["pptop10"]:
#     mergebench["relative_bench"] = "lower"
# else:
#     mergebench["relative_bench"] = "higher"
mergebench = mergebench[
    [
        "Publication_year",
        "Subject_category",
        "Prop_papers",
        "pptop10",
        "Full_bench",
        "relative_bench",
    ]
]
# print(mergebench)
mergebench["relative_bench"] = mergebench["relative_bench"].astype(str)
mergebench = mergebench.replace("True", "PP(top10) exceeds Swedish Benchmark")
mergebench = mergebench.replace("False", "PP(top10) does not exceed Swedish Benchmark")


# # Each field will be a different line. Need to subset by field
biochemresmeth_trend = mergebench[
    (mergebench["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")
]
biochemmolec_trend = mergebench[
    (mergebench["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")
]
biotech_trend = mergebench[
    (mergebench["Subject_category"] == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY")
]
oncology_trend = mergebench[(mergebench["Subject_category"] == "ONCOLOGY")]
cellbio_trend = mergebench[(mergebench["Subject_category"] == "CELL BIOLOGY")]
genetics_trend = mergebench[(mergebench["Subject_category"] == "GENETICS & HEREDITY")]


trendcolours = [
    SCILIFE_COLOURS[0],
    SCILIFE_COLOURS[4],
    SCILIFE_COLOURS[8],
    SCILIFE_COLOURS[12],
    SCILIFE_COLOURS[1],
    SCILIFE_COLOURS[14],
]

benchcolours = [SCILIFE_COLOURS[16], SCILIFE_COLOURS[18]]


# make figure
# fig = go.Figure()
# Add traces - each line a different trace
fig = px.scatter(
    mergebench,
    x="Publication_year",
    y="Prop_papers",
    # set the size of the marker by impact value
    size="pptop10",
    # set the colour of the maker by impact value
    color="relative_bench",
    color_discrete_sequence=benchcolours,
)
fig.update_traces(
    #    marker=dict(size=20, line=dict(width=2, color="black")),
    marker=dict(line=dict(width=2, color="black")),
    cliponaxis=False,
    opacity=1,
)
fig.add_trace(
    go.Scatter(
        name="Biochemical Research Methods",
        x=biochemresmeth_trend.Publication_year,
        y=biochemresmeth_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[0]),
        line=dict(color=trendcolours[0], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Biochemistry & Molecular Biology",
        x=biochemmolec_trend.Publication_year,
        y=biochemmolec_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[1]),
        line=dict(color=trendcolours[1], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Biotechnology & Applied Microbiology",
        x=biotech_trend.Publication_year,
        y=biotech_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[2]),
        line=dict(color=trendcolours[2], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Oncology",
        x=oncology_trend.Publication_year,
        y=oncology_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[3]),
        line=dict(color=trendcolours[3], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Cell Biology",
        x=cellbio_trend.Publication_year,
        y=cellbio_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[4]),
        line=dict(color=trendcolours[4], width=2),
    )
)
fig.add_trace(
    go.Scatter(
        name="Genetics & Heredity",
        x=genetics_trend.Publication_year,
        y=genetics_trend.Prop_papers,
        mode="lines",
        marker=dict(color=trendcolours[5]),
        line=dict(color=trendcolours[5], width=2),
    )
)
fig.update_layout(
    plot_bgcolor="white",
    autosize=False,
    font=dict(size=18),
    margin=dict(r=350, t=0, b=0, l=0),
    width=1800,
    height=1000,
    showlegend=True,
)
fig.update_layout(
    legend=dict(
        yanchor="top",
        # y=0.99,
        xanchor="right",
        title=" ",
        x=1.45,
    )
)
Years = mergebench["Publication_year"].unique().astype(str)
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

highest_y_value = max(mergebench["Prop_papers"])

if highest_y_value < 0.3:
    yaxis_tick = 0.05
if highest_y_value > 0.5:
    yaxis_tick = 0.2


fig.update_yaxes(
    title=" ",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    dtick=yaxis_tick,
    range=[0, 0.3],
)
if not os.path.isdir("Plots/"):
    os.mkdir("Plots/")
# fig.show()
fig.write_image("Plots/facilities_trends_arttypes.svg")
fig.write_image("Plots/facilities_trends_arttypes.png")
