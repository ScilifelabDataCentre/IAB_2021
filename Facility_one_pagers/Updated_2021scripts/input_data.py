import pandas as pd
import numpy as np


### FAC MAP
# to their labels in the publication database
fac_map_input = pd.read_excel(
    "IAB2021data/Reporting Units 2020.xlsx",
    sheet_name="Reporting units",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)
fac_map_input["PDB label"] = fac_map_input["PDB label"].str.replace(
    r"\(.*\)", "", regex=True
)
fac_map_input = fac_map_input[["Unit", "PDB label"]]
fac_map_input = fac_map_input.replace("", np.nan)
fac_map_input["PDB label"] = fac_map_input["PDB label"].fillna(fac_map_input["Unit"])
fac_map_input.rename(columns={"PDB label": "Label"}, inplace=True)
fac_map = dict(zip(fac_map_input.Label, fac_map_input.Unit))

### AFFILIATES
# Years of interest in 2021 - 2018-20
# This data will be used in the
# We have 3 data files from OO for this

aff_2018_raw = pd.read_excel(
    "IAB2021data/Infrastructure Users 2018 QC.xlsx",
    sheet_name="Facility Users, doubl. removed",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

aff_2019_raw = pd.read_excel(
    "IAB2021data/Infrastructure Users 2019 QC.xlsx",
    sheet_name="Facility Users, doubl. removed",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

aff_2020_raw = pd.read_excel(
    "IAB2021data/Infrastructure Users 2020 QC.xlsx",
    sheet_name="Facility users, doubl. removed",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Want to get counts of how many of each individual affiliation
# for each unit

affiliates_data_2018 = (
    aff_2018_raw.groupby(["Unit", "PI affiliation"]).size().reset_index()
)
affiliates_data_2019 = (
    aff_2019_raw.groupby(["Unit", "PI affiliation"]).size().reset_index()
)
affiliates_data_2020 = (
    aff_2020_raw.groupby(["Unit", "PI affiliation"]).size().reset_index()
)

affiliates_data_2018.columns = ["Unit", "PI_aff", "Count"]
affiliates_data_2019.columns = ["Unit", "PI_aff", "Count"]
affiliates_data_2020.columns = ["Unit", "PI_aff", "Count"]

affiliates_data_2018.insert(loc=2, column="Year", value="2018")
affiliates_data_2019.insert(loc=2, column="Year", value="2019")
affiliates_data_2020.insert(loc=2, column="Year", value="2020")

aff_comb = pd.concat([affiliates_data_2018, affiliates_data_2019, affiliates_data_2020])

# Now need to replace all of the affiliation names with a shortened version

aff_map_abbr = {
    "Chalmers University of Technology": "Chalmers",
    "KTH Royal Institute of Technology": "KTH",
    "Swedish University of Agricultural Sciences": "SLU",
    "Karolinska Institutet": "KI",
    "Linköping University": "LiU",
    "Lund University": "LU",
    "Naturhistoriska Riksmuséet": "NRM",
    "Stockholm University": "SU",
    "Umeå University": "UmU",
    "University of Gothenburg": "GU",
    "Uppsala University": "UU",
    "Örebro University": "ÖU",
    "International University": "Int Univ",
    "Other Swedish University": "Other Swe Univ",
    "Other Swedish organization": "Other Swe Org",
    "Other international organization": "Other Int Org",
    "Industry ": "Industry",
    "Industry": "Industry",
    "Healthcare": "Healthcare",
}

affiliate_data = aff_comb.replace(aff_map_abbr, regex=True)

### FACILITY DATA
# Single data contains all basic data for fac
# Read in to pdf almost directly
# rename columns for clarity
Facility_data = pd.read_excel(
    "IAB2021data/Single data 2020.xlsx",
    sheet_name="Single Data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Facility_data.rename(
    columns={
        "Facility Director": "FD",
        "Head of Facility": "HOF",
        "SciLifeLab facility since": "SLL_since",
        "Host university": "H_uni",
        "FTEs financed by Scilifelab": "SLL_FTEs",
        "Funding 2020 SciLifeLab (kSEK)": "Amount (kSEK)",
        "Reource allocation 2020 Acadmia (national)": "RA_nat",
        "Reource allocation 2020 Acadmia (international)": "RA_int",
        "Reource allocation 2020 Internal tech. dev.": "RA_tech",
        "Reource allocation 2020 Industry": "RA_Ind",
        "Reource allocation 2020 Healthcare": "RA_Health",
        "Reource allocation 2020 Other gov. agencies": "RA_ogov",
        "User Fees 2020 Total (kSEK)": "UF_Tot",
        "User fees academic Sweden": "UF_Swe",
        "User fees academic international": "UF_Int",
        "User fees industry": "UF_ind",
        "User fees healthcare": "UF_health",
        "User fees other": "UF_oth",
        "User fees by sector 2020 Academia (national)": "UF_sect_nat",
        "User fees by sector 2020 Academia (international)": "UF_sect_int",
        "User fees by sector 2020 Industry": "UF_sect_ind",
        "User fees by sector 2020 Healthcare": "UF_sect_health",
        "User fees by sector 2020 Other gov. agencies": "UF_sect_othgov",
    },
    inplace=True,
)

### FUNDING
# This involves data from 'other funding' and 'single data'
# both files provided by OO
# Need to add SLL funding to other funding data and get a total

other_funding = pd.read_excel(
    "IAB2021data/Other funding 2020.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Some funding info also included in the facility data
# extract SLL funding data from single(facility) data

SLL_funding = Facility_data[["Facility", "Platform", "Amount (kSEK)"]]
SLL_funding.insert(loc=2, column="Financier", value="SciLifeLab")

# now concatenate this with other funding
# also calculate total funding
Funding_comb = pd.concat([SLL_funding, other_funding])
tot_fund = Funding_comb.groupby(["Facility"]).sum().reset_index()
tot_fund.insert(loc=2, column="Financier", value="Total")
Funding = pd.concat([Funding_comb, tot_fund])

###PUBLICATIONS!
# Used in the two graphs for one-pagers
# Need to use this data in 2 ways:
# (1) Make the barplot with JIF scores
# (2) Make a barplot of publications by category
# whilst the rest of the data comes from OO,
# This data is taken from:
# (1) publications database
# (2) publications db and JIF scores (from J. Rung)
# import raw publications data

# Focus on data for (1) - extract individual labels for records from pub db

Pubs_cat_raw = pd.read_excel(
    "IAB2021data/Pub_18to20_indivlab_20210415.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need to get data for (fac) and groupby

pub_sub = Pubs_cat_raw[["Year", "Labels", "Qualifiers"]]
pub_sub = pub_sub.replace(r"^\s*$", "No category", regex=True)
pub_sub["Qualifiers"] = pub_sub["Qualifiers"].astype("category")

pub_cat_group = pub_sub.groupby(["Year", "Labels", "Qualifiers"]).size().reset_index()

pub_cat_group["Labels"] = pub_cat_group["Labels"].str.replace(r"\(.*\)", "", regex=True)

pub_cat_data_basic = pub_cat_group.replace(fac_map, regex=True)

# Need to duplcate values for mass cytometry to give both LiU and KI

pub_cat_data_needmc = pub_cat_data_basic[
    (pub_cat_data_basic["Labels"] == "Mass Cytometry (LiU)")
]

pub_cat_data_needmc = pub_cat_data_needmc.replace(
    "Mass Cytometry (LiU)", "Mass Cytometry (KI)"
)

pub_concat_data = pd.concat([pub_cat_data_basic, pub_cat_data_needmc])

pub_concat_data.columns = ["Year", "Unit", "Qualifiers", "Count"]

pub_cat_data = pub_concat_data

# Now for data for (2)
# This time work with pub data with labels combined
# i.e. one record per publication

Pubs_JIF_raw = pd.read_excel(
    "IAB2021data/Pub_18to20_20210415.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

JIF_scores_raw = pd.read_excel(
    "IAB2021data/JIFscoresheet_20210415.xlsx",
    sheet_name="DJR_5847",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

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

# Match this to the database with the labels seperated (easiest way to seperate out labels)

JIF_merge_fullnames_sub = JIF_merge_fullnames[["Title", "JIF"]]

Pubs_cat_low = Pubs_cat_raw

Pubs_cat_low["Title"] = Pubs_cat_low["Title"].str.lower()

match_JIF_seplabs = pd.merge(
    Pubs_cat_low,
    JIF_merge_fullnames_sub,
    how="left",
    on="Title",
)

match_JIF_seplabs["JIF"] = match_JIF_seplabs["JIF"].fillna(-1)
match_JIF_seplabs["JIF"] = pd.to_numeric(match_JIF_seplabs["JIF"])
match_JIF_seplabs["JIFcat"] = pd.cut(
    match_JIF_seplabs["JIF"],
    bins=[-1, 0, 6, 9, 25, 1000],
    include_lowest=True,
    labels=["JIF unknown", "JIF <6", "JIF 6-9", "JIF 9-25", "JIF >25"],
)

# replace facility labels

match_JIF_seplabs["Labels"] = match_JIF_seplabs["Labels"].str.replace(
    r"\(.*\)", "", regex=True
)

JIF_match_basic = match_JIF_seplabs.replace(fac_map, regex=True)

# Need to do a group by and check the sums work! (and align with above pub numbers)

JIF_sub = JIF_match_basic[["Year", "Labels", "JIFcat"]]

JIF_sub_group = JIF_sub.groupby(["Year", "Labels", "JIFcat"]).size().reset_index()

JIF_sub_group.columns = ["Year", "Unit", "JIFcat", "Count"]

JIF_needmc = JIF_sub_group[(JIF_sub_group["Unit"] == "Mass Cytometry (LiU)")]

JIF_needmc = JIF_needmc.replace("Mass Cytometry (LiU)", "Mass Cytometry (KI)")

JIF_data = pd.concat([JIF_sub_group, JIF_needmc])

# As a check, can compare publications data divided by category and JIF for each unit
# The total numbers for each unit and for each year should align.
# JIF_data.to_excel("Check_JIFdata.xlsx")
# pub_cat_data.to_excel("Check_pubcatdata.xlsx")
