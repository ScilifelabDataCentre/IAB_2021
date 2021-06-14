"""Make the table to find the three subject categories that each facility works most on.
Use some of data for bubble plot focussing on top 6 categories"""
import pandas as pd
import numpy as np
from collections import Counter
import plotly.graph_objects as go
from colour_science_2020 import (
    SCILIFE_COLOURS,
)

# need datafile with unit names (from our extraction)
facs_unitnames = pd.read_excel(
    "Data/Facilities_20210419.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need datafile with DOI and UT in it, so that we can link the unit names and subject fields -from KTH
Facilities_UI = pd.read_excel(
    "Data/SciLifeLab-facilities-20210512.xlsx",
    sheet_name="publ_data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# First match unit name data to get it UT assigned
Facilities_UI = Facilities_UI[["UT", "DOI"]]

Facs_fieldandUI = pd.merge(
    facs_unitnames,
    Facilities_UI,
    how="left",
    on="DOI",
)

# Facs_fieldandUI.to_excel("testmatchfacDOI.xlsx")
# Need to manually go through - no DOI leads to multiple matches and can improve matches in some cases
# add corrected file
Facilities_imp = pd.read_excel(
    "Data/testmatchfacDOI_manuallyedited.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Facilities_imp.drop_duplicates(subset="UT", keep="first", inplace=True)
# one 'blank' UT will remain, but next step is to match on UT, and other files will not contain a 'blank', so it will not match
# Facilities_imp.to_excel("check.xlsx")

Facilities_imp_sub = Facilities_imp[["UT", "Labels"]]

# need datafile with subject fields in from KTH
facs_fields = pd.read_excel(
    "Data/SciLifeLab_cf_subj_cat_facilities.xlsx",
    sheet_name="SciLifeLab_cf_subj_cat_faciliti",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Facs_fieldandunit = pd.merge(
    facs_fields,
    Facilities_imp_sub,
    how="left",
    on="UT",
)

# print(Facs_fieldandunit.info())

Facs_fieldandunit_sub = Facs_fieldandunit[
    (Facs_fieldandunit["Publication_year"] > 2012)
    & (Facs_fieldandunit["Publication_year"] < 2021)
]

Facs_fieldandunit_sub = Facs_fieldandunit_sub[["Subject_category", "Labels"]]


# print(Facs_fieldandunit_sub.info())
# Now see what each facility works on
facilities_list = [
    # "Bioinformatics Compute and Storage",
    "Bioinformatics Long-term Support WABI",
    "Bioinformatics Support and Infrastructure",
    "Systems Biology",
    "Advanced Light Microscopy",
    "BioImage Informatics",
    "Cell Profiling",
    "Cryo-EM",
    "Swedish NMR Centre",
    "Chemical Biology Consortium Sweden",
    "Genome Engineering Zebrafish",
    "HTGE",
    "Clinical Genomics Gothenburg",
    "Clinical Genomics Linköping",
    "Clinical Genomics Lund",
    "Clinical Genomics Stockholm",
    # no pubs -"Clinical Genomics Umeå",
    "Clinical Genomics Uppsala",
    "Clinical Genomics Örebro",
    "Drug Discovery and Development",
    # no pubs "Ancient DNA",
    "ESCG",
    "In Situ Sequencing",
    "Microbial Single Cell Genomics",
    "National Genomics Infrastructure",
    "Autoimmunity and Serology Profiling",
    "Chemical Proteomics",
    "Mass Cytometry",
    "PLA and Single Cell Proteomics",
    "Proteogenomics",
    "Swedish Metabolomics Centre",
    "Translational Plasma Profiling",
]

facilities_official = [
    # "Compute and Storage",
    "Long-term Support (WABI)",
    "Support and Infrastructure",
    "Systems Biology",
    "Advanced Light Microscopy",
    "BioImage Informatics",
    "Cell Profiling",
    "Cryo-EM",
    "Swedish NMR Centre",
    "Chemical Biology Consortium Sweden",
    "Genome Engineering Zebrafish",
    "High Throughput Genome Engineering",
    "Clinical Genomics Gothenburg",
    "Clinical Genomics Linköping",
    "Clinical Genomics Lund",
    "Clinical Genomics Stockholm",
    # no pubs -"Clinical Genomics Umeå",
    "Clinical Genomics Uppsala",
    "Clinical Genomics Örebro",
    "Drug Discovery and Development",
    # no pubs "Ancient DNA",
    "Eukaryotic Single Cell Genomics",
    "In Situ Sequencing",
    "Microbial Single Cell Genomics",
    "National Genomics Infrastructure",
    "Autoimmunity and Serology Profiling",
    "Chemical Proteomics",
    "Mass Cytometry",
    "PLA and Single Cell Proteomics",
    "Proteogenomics",
    "Swedish Metabolomics Centre",
    "Translational Plasma Profiling",
]


def str_cat(x):
    return x.str.cat(sep=", ")


values = Facs_fieldandunit_sub[
    Facs_fieldandunit_sub["Labels"].str.contains(facilities_list[0])
]
values = (
    values.groupby("Subject_category")
    .count()
    .reset_index()
    .sort_values(by="Labels", ascending=False)
    .head(3)
)
values["Unit"] = facilities_official[0]
df = values.groupby("Unit").agg(field_list=("Subject_category", str_cat))
df = df.reset_index()


for i in range(1, 29):
    values = Facs_fieldandunit_sub[
        Facs_fieldandunit_sub["Labels"].str.contains(facilities_list[i])
    ]
    values = (
        values.groupby("Subject_category")
        .count()
        .reset_index()
        .sort_values(by="Labels", ascending=False)
        .head(3)
    )
    values["Unit"] = facilities_official[i]
    df1 = values.groupby("Unit").agg(field_list=("Subject_category", str_cat))
    df1 = df1.reset_index()
    df = pd.concat([df, df1])
# print(df)

# EDIT STRINGS AS NEEDED TO IMPROVE LEGIBILITY

df["field_list"] = df["field_list"].replace(
    "BIOCHEMICAL RESEARCH METHODS, CELL BIOLOGY, ENGINEERING, ELECTRICAL & ELECTRONIC",
    "BIOCHEMICAL RESEARCH METHODS, CELL BIOLOGY, ENGINEERING (ELECTRICAL & ELECTRONIC)",
)

df["field_list"] = df["field_list"].replace(
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY, MULTIDISCIPLINARY, CHEMISTRY, PHYSICAL",
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY (MULTIDISCIPLINARY), CHEMISTRY (PHYSICAL)",
)

df["field_list"] = df["field_list"].replace(
    "CHEMISTRY, MEDICINAL, BIOCHEMISTRY & MOLECULAR BIOLOGY, PHARMACOLOGY & PHARMACY",
    "CHEMISTRY (MEDICINAL), BIOCHEMISTRY & MOLECULAR BIOLOGY, PHARMACOLOGY & PHARMACY",
)

df["field_list"] = df["field_list"].replace(
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, ENGINEERING, ENVIRONMENTAL, ENVIRONMENTAL SCIENCES",
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, ENGINEERING (ENVIRONMENTAL), ENVIRONMENTAL SCIENCES",
)

df["field_list"] = df["field_list"].replace(
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY, MULTIDISCIPLINARY, ENDOCRINOLOGY & METABOLISM",
    "BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY (MULTIDISCIPLINARY), ENDOCRINOLOGY & METABOLISM",
)

df["field_list"] = df["field_list"].replace(
    "CHEMISTRY, ORGANIC, BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY, MEDICINAL",
    "CHEMISTRY (ORGANIC), BIOCHEMISTRY & MOLECULAR BIOLOGY, CHEMISTRY (MEDICINAL)",
)

# Write into table
fig = go.Figure(
    data=[
        go.Table(
            columnwidth=[100, 300],
            header=dict(
                values=[
                    "<b>Unit</b>",
                    "<b>Subject Category</b>",
                ],
                align=["left", "left"],
                fill_color=SCILIFE_COLOURS[0],
                font=dict(color="black", size=14),
                line=dict(width=0),
            ),
            cells=dict(
                values=(
                    df["Unit"],
                    df["field_list"],
                ),
                align=["left", "left"],
                fill_color=[[SCILIFE_COLOURS[1], "white"] * 20],
                font=dict(color="black", size=12),
                height=30,
                line=dict(width=0),
            ),
        )
    ]
)
# fig.show()
fig.update_layout(autosize=False, margin={"l": 0, "r": 0, "t": 0, "b": 0}, height=1350)
fig.write_image("Plots/Main3categories_unit_nocs.png")
fig.write_image("Plots/Main3categories_unit_nocs.svg")
