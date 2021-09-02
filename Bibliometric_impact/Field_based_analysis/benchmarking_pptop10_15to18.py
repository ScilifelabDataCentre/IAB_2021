import pandas as pd
import numpy as np
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
import os


benchmark = pd.read_excel(
    "Data/SciLifeLab_swe_benchmark.xlsx",
    sheet_name="SciLifeLab_swe_benchmark",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

affiliates = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_byaddress-2.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_byaddres",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


facilities = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_facilities.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_faciliti",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# For now, calculate full counts and compare full counts to Swedish full counts
# can use cf or PPtop10 to benchmark (PPtop10 probably more comparable with everything else in report)
# Focus on latest (2018, as of IAB 2021) impact values

benchmark_compare = benchmark[
    ["Publication_year", "Subject_category", "Prop_Top10_scxwo_full", "cf_scxwo_full"]
]
benchmark_compare = benchmark_compare[
    (benchmark_compare["Publication_year"] == 2015)
    | (benchmark_compare["Publication_year"] == 2016)
    | (benchmark_compare["Publication_year"] == 2017)
    | (benchmark_compare["Publication_year"] == 2018)
]

bench_pp_fields = (
    benchmark_compare.groupby("Subject_category")["Prop_Top10_scxwo_full"]
    .mean()
    .reset_index()
)


# print(bench_pp_fields)

aff_sub = affiliates[
    [
        "Publication_year",
        "Subject_category",
        "Top10_scxwo",
        "Doc_type_code_rev",
    ]
]
aff_201518 = aff_sub[
    (aff_sub["Publication_year"] == 2015)
    | (aff_sub["Publication_year"] == 2016)
    | (aff_sub["Publication_year"] == 2017)
    | (aff_sub["Publication_year"] == 2018)
]
aff_201518 = aff_201518[
    (aff_201518["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")
    | (aff_201518["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")
    | (aff_201518["Subject_category"] == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY")
    | (aff_201518["Subject_category"] == "ONCOLOGY")
    | (aff_201518["Subject_category"] == "CELL BIOLOGY")
    | (aff_201518["Subject_category"] == "GENETICS & HEREDITY")
]
aff_201518 = aff_201518[
    (aff_201518["Doc_type_code_rev"] == "RV")
    | (aff_201518["Doc_type_code_rev"] == "AR")
    | (aff_201518["Doc_type_code_rev"] == "PP")
]

aff_201518["Top10_scxwo"] = aff_201518["Top10_scxwo"].astype(float)

aff_pp_fields = (
    aff_201518.groupby("Subject_category")["Top10_scxwo"].mean().reset_index()
)
aff_pp_fields = aff_pp_fields.rename(
    columns={
        "Top10_scxwo": "aff_pp",
    }
)


fac_sub = facilities[
    ["Publication_year", "Subject_category", "Top10_scxwo", "Doc_type_code_rev"]
]
fac_201518 = fac_sub[
    (fac_sub["Publication_year"] == 2015)
    | (fac_sub["Publication_year"] == 2016)
    | (fac_sub["Publication_year"] == 2017)
    | (fac_sub["Publication_year"] == 2018)
]
fac_201518 = fac_201518[
    (fac_201518["Subject_category"] == "BIOCHEMICAL RESEARCH METHODS")
    | (fac_201518["Subject_category"] == "BIOCHEMISTRY & MOLECULAR BIOLOGY")
    | (fac_201518["Subject_category"] == "BIOTECHNOLOGY & APPLIED MICROBIOLOGY")
    | (fac_201518["Subject_category"] == "ONCOLOGY")
    | (fac_201518["Subject_category"] == "CELL BIOLOGY")
    | (fac_201518["Subject_category"] == "GENETICS & HEREDITY")
]
fac_201518 = fac_201518[
    (fac_201518["Doc_type_code_rev"] == "RV")
    | (fac_201518["Doc_type_code_rev"] == "AR")
    | (fac_201518["Doc_type_code_rev"] == "PP")
]

fac_201518["Top10_scxwo"] = fac_201518["Top10_scxwo"].astype(float)

fac_pp_fields = (
    fac_201518.groupby("Subject_category")["Top10_scxwo"].mean().reset_index()
)
fac_pp_fields = fac_pp_fields.rename(
    columns={
        "Top10_scxwo": "fac_pp",
    }
)


comb_Bandaff = pd.merge(
    bench_pp_fields,
    aff_pp_fields,
    how="left",
    on=["Subject_category"],
)
comb_all = pd.merge(
    comb_Bandaff,
    fac_pp_fields,
    how="left",
    on=["Subject_category"],
)

comb_all["Prop_Top10_scxwo_full"] = comb_all["Prop_Top10_scxwo_full"] * 100
comb_all["aff_pp"] = comb_all["aff_pp"] * 100
comb_all["fac_pp"] = comb_all["fac_pp"] * 100
print(comb_all)
fig = go.Figure(
    data=[
        go.Bar(
            name="Sweden",
            x=comb_all.Subject_category,
            y=comb_all.Prop_Top10_scxwo_full,
            marker=dict(color="#4C979F", line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="Affiliated Researchers",
            x=comb_all.Subject_category,
            y=comb_all.aff_pp,
            marker=dict(color="#A7C947", line=dict(color="#000000", width=1)),
        ),
        go.Bar(
            name="Infrastructure Users",
            x=comb_all.Subject_category,
            y=comb_all.fac_pp,
            marker=dict(color="#491F53", line=dict(color="#000000", width=1)),
        ),
    ]
)


fig.update_layout(
    barmode="group",
    plot_bgcolor="white",
    font=dict(size=39),
    margin=dict(r=150, l=10),
    autosize=False,
    width=1800,
    height=1200,
    legend_title_text=" <b>Publication Group</b>",
)
# modify x-axis
fig.update_xaxes(title=" ", showgrid=True, linecolor="black")
# modify y-axis
fig.update_yaxes(
    title=" ",
    showgrid=True,
    gridcolor="lightgrey",
    linecolor="black",
    ticktext=["0", "10", "20", "30", "40"],
    tickvals=["0", "10", "20", "30", "40"],
    range=[0, 41],
)
fig.show()
if not os.path.isdir("Plots/largerfonts/"):
    os.mkdir("Plots/largerfonts/")
fig.write_image("Plots/largerfonts/benchmark_1518_pptop10.svg")
fig.write_image("Plots/largerfonts/benchmark_1518_pptop10.png")
