import pandas as pd


Pubs_JIF_raw = pd.read_excel(
    "DataforJIF/Fellows_20210419.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

JIF_scores_raw = pd.read_excel(
    "DataforJIF/JIFscoresheet_modforallyears_ori20210415.xlsx",
    sheet_name="DJR_5847",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need to filter raw pubs (2014-20 for IAB 2021)

Pubs_JIF_raw = Pubs_JIF_raw[
    (Pubs_JIF_raw["Year"] > 2013) & (Pubs_JIF_raw["Year"] < 2021)
]

# Need to join the two above files and align JIF with ISSN/ISSN-L
# simpler to work with only columns of interest

Pubs_JIF_sub = Pubs_JIF_raw[
    [
        "Title",
        "Year",
        "Labels",
        "Journal",
        "ISSN",
        "ISSN-L",
    ]
]

JIF_scores_sub = JIF_scores_raw[
    [
        "ISSN",
        "Full Journal Title",
        "JCR Abbreviated Title",
        "Impact Factor without Journal Self Cites",
    ]
]

# Must maximise matching of JIF. I recommend checking over
# May be necessary to do some manual work

Pubs_JIF_sublow = Pubs_JIF_sub.apply(lambda x: x.astype(str).str.lower())
JIF_scores_sublow = JIF_scores_sub.apply(lambda x: x.astype(str).str.lower())
Pubs_JIF_sublow["Journal"] = Pubs_JIF_sublow["Journal"].str.replace(".", "", regex=True)
JIF_scores_sublow["JCR Abbreviated Title"] = JIF_scores_sublow[
    "JCR Abbreviated Title"
].str.replace("-basel", "", regex=True)

JIF_merge = pd.merge(
    Pubs_JIF_sublow,
    JIF_scores_sublow,
    how="left",
    on="ISSN",
)

JIF_mergebackori = pd.merge(
    Pubs_JIF_sublow,
    JIF_merge,
    on=[
        "Title",
        "Year",
        "Labels",
        "Journal",
        "ISSN",
        "ISSN-L",
    ],
)

JIF_mergebackori.drop_duplicates(subset="Title", keep="first", inplace=True)

JIF_merge_ISSNL = pd.merge(
    JIF_mergebackori,
    JIF_scores_sublow,
    how="left",
    left_on="ISSN-L",
    right_on="ISSN",
)

JIF_merge_ISSNL.drop_duplicates(subset="Title", keep="first", inplace=True)

JIF_merge_ISSNL["Impact Factor without Journal Self Cites_x"] = JIF_merge_ISSNL[
    "Impact Factor without Journal Self Cites_x"
].fillna(JIF_merge_ISSNL["Impact Factor without Journal Self Cites_y"])

JIF_merge_ISSNL = JIF_merge_ISSNL.drop(
    [
        "ISSN_y",
        "Full Journal Title_y",
        "JCR Abbreviated Title_y",
        "Impact Factor without Journal Self Cites_y",
    ],
    axis=1,
)

# now attempt to match on journal names

JIF_merge_abbnames = pd.merge(
    JIF_merge_ISSNL,
    JIF_scores_sublow,
    how="left",
    left_on="Journal",
    right_on="JCR Abbreviated Title",
)

JIF_merge_abbnames["Impact Factor without Journal Self Cites_x"] = JIF_merge_abbnames[
    "Impact Factor without Journal Self Cites_x"
].fillna(JIF_merge_abbnames["Impact Factor without Journal Self Cites"])

JIF_merge_abbnames.drop_duplicates(subset="Title", keep="first", inplace=True)

JIF_merge_abbnames = JIF_merge_abbnames.drop(
    [
        "ISSN",
        "Full Journal Title",
        "JCR Abbreviated Title",
        "Impact Factor without Journal Self Cites",
    ],
    axis=1,
)

JIF_merge_fullnames = pd.merge(
    JIF_merge_abbnames,
    JIF_scores_sublow,
    how="left",
    left_on="Journal",
    right_on="Full Journal Title",
)

JIF_merge_fullnames.drop_duplicates(subset="Title", keep="first", inplace=True)

JIF_merge_fullnames["Impact Factor without Journal Self Cites_x"] = JIF_merge_fullnames[
    "Impact Factor without Journal Self Cites_x"
].fillna(JIF_merge_fullnames["Impact Factor without Journal Self Cites"])

JIF_merge_fullnames = JIF_merge_fullnames.drop(
    [
        "ISSN",
        "Full Journal Title",
        "JCR Abbreviated Title",
        "Impact Factor without Journal Self Cites",
    ],
    axis=1,
)

## below prints out a file that can be checked to determine whether
## manual work may increase the number of matches

JIF_merge_fullnames.rename(
    columns={
        "ISSN_x": "ISSN",
        "Full Journal Title_x": "Full Journal Title",
        "JCR Abbreviated Title_x": "JCR Abbreviated Title",
        "Impact Factor without Journal Self Cites_x": "JIF",
    },
    inplace=True,
)

JIF_merge_fullnames.to_excel("Check_me_manual_improve.xlsx")

# segment up the JIFs to groups
JIF_merge_fullnames["JIF"] = JIF_merge_fullnames["JIF"].fillna(-1)

JIF_merge_fullnames["JIF"] = pd.to_numeric(JIF_merge_fullnames["JIF"])
JIF_merge_fullnames["JIFcat"] = pd.cut(
    JIF_merge_fullnames["JIF"],
    bins=[-1, 0, 6, 9, 25, 1000],
    include_lowest=True,
    labels=["JIF unknown", "JIF <6", "JIF 6-9", "JIF 9-25", "JIF >25"],
)

# Need to do a group by and check the sums work

JIF_sub = JIF_merge_fullnames[["Year", "Labels", "JIFcat"]]

JIF_sub_group_fell = JIF_sub.groupby(["Year", "JIFcat"]).size().reset_index()

JIF_sub_group_fell.columns = ["Year", "JIFcat", "Count"]


# Use this to check that the sums are as expected given the original publication files
# JIF_sub_group_fell.to_excel("fellows_JIF_groups.xlsx")
