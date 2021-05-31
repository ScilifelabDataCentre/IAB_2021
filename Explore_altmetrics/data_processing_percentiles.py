"""process data to get proportion of publications in the 90% percentile in terms of altmetrics scores"""
import pandas as pd
import numpy as np

Aff_alt_data = pd.read_excel(
    "Data/Altmetrics-SciLifelab_20210521.xlsx",
    sheet_name="Affiliated",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Fac_alt_data = pd.read_excel(
    "Data/Altmetrics-SciLifelab_20210521.xlsx",
    sheet_name="Facilities",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

Fell_alt_data = pd.read_excel(
    "Data/Altmetrics-SciLifelab_20210521.xlsx",
    sheet_name="Fellows",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# we can place these things in context of everything of same age and same age and journal in the Altmetrics database
# think that percentile is a good option for comparison (especially as we can look at 90th percentile and get top 10)
# context:similar_age_3m:pct - percentile in context of whole database in last 3 months
# context:similar_age_journal_3m:pct - percentile in context of things in same journal in last 3 months

####### AFFILIATES

# get percentile data for all
Aff_alt_data_all = Aff_alt_data[["UT", "Year", "context:similar_age_3m:pct"]]
Aff_alt_data_all = Aff_alt_data_all.replace("", np.nan)
Aff_alt_data_all = Aff_alt_data_all.dropna(axis=0)
Aff_alt_data_all["all_top10"] = Aff_alt_data_all["context:similar_age_3m:pct"] >= 90
Aff_alt_data_all["all_top10"] = Aff_alt_data_all["all_top10"].astype(str)
Aff_alt_data_all["all_top10"] = Aff_alt_data_all["all_top10"].replace("True", 1)
Aff_alt_data_all["all_top10"] = Aff_alt_data_all["all_top10"].replace("False", 0)
# percentile data for journal
Aff_alt_data_j = Aff_alt_data[["UT", "Year", "context:similar_age_journal_3m:pct"]]
Aff_alt_data_j = Aff_alt_data_j.replace("", np.nan)
Aff_alt_data_j = Aff_alt_data_j.dropna(axis=0)
Aff_alt_data_j["j_top10"] = Aff_alt_data_j["context:similar_age_journal_3m:pct"] >= 90
Aff_alt_data_j["j_top10"] = Aff_alt_data_j["j_top10"].astype(str)
Aff_alt_data_j["j_top10"] = Aff_alt_data_j["j_top10"].replace("True", 1)
Aff_alt_data_j["j_top10"] = Aff_alt_data_j["j_top10"].replace("False", 0)
# merge the two together based on UT and year
Aff_data = pd.merge(
    Aff_alt_data_all,
    Aff_alt_data_j,
    on=["UT", "Year"],
)
Aff_data = Aff_data[(Aff_data["Year"] > 2012) & (Aff_data["Year"] < 2021)]
Aff_data.drop_duplicates(subset="UT", keep="first", inplace=True)
Aff_data = Aff_data.drop(
    [
        "UT",
        "context:similar_age_3m:pct",
        "context:similar_age_journal_3m:pct",
    ],
    axis=1,
)
# Aff_data.to_excel("test_aff.xlsx")
Aff_data_group = Aff_data.groupby(["Year"]).mean().reset_index()
Aff_data_group = Aff_data_group.rename(
    columns={
        "all_top10": "Comparable Age Only",
        "j_top10": "Comparable Age in Same Journal",
    }
)
# melt it to create correct format for grouped barchart
Aff_data_group_melt = pd.melt(
    Aff_data_group,
    id_vars="Year",
    value_vars=list(Aff_data_group.columns[1:]),
    var_name="Context_type",
    value_name="Prop_90_pct",
)

Aff_data_group_melt["Percent"] = Aff_data_group_melt["Prop_90_pct"] * 100

# print(Aff_data_group_melt.head(16))
####### Facilities

# get percentile data for all
Fac_alt_data_all = Fac_alt_data[["UT", "Year", "context:similar_age_3m:pct"]]
Fac_alt_data_all = Fac_alt_data_all.replace("", np.nan)
Fac_alt_data_all = Fac_alt_data_all.dropna(axis=0)
Fac_alt_data_all["all_top10"] = Fac_alt_data_all["context:similar_age_3m:pct"] >= 90
Fac_alt_data_all["all_top10"] = Fac_alt_data_all["all_top10"].astype(str)
Fac_alt_data_all["all_top10"] = Fac_alt_data_all["all_top10"].replace("True", 1)
Fac_alt_data_all["all_top10"] = Fac_alt_data_all["all_top10"].replace("False", 0)
# percentile data for journal
Fac_alt_data_j = Fac_alt_data[["UT", "Year", "context:similar_age_journal_3m:pct"]]
Fac_alt_data_j = Fac_alt_data_j.replace("", np.nan)
Fac_alt_data_j = Fac_alt_data_j.dropna(axis=0)
Fac_alt_data_j["j_top10"] = Fac_alt_data_j["context:similar_age_journal_3m:pct"] >= 90
Fac_alt_data_j["j_top10"] = Fac_alt_data_j["j_top10"].astype(str)
Fac_alt_data_j["j_top10"] = Fac_alt_data_j["j_top10"].replace("True", 1)
Fac_alt_data_j["j_top10"] = Fac_alt_data_j["j_top10"].replace("False", 0)
# merge the two together based on UT and year
Fac_data = pd.merge(
    Fac_alt_data_all,
    Fac_alt_data_j,
    on=["UT", "Year"],
)
Fac_data = Fac_data[(Fac_data["Year"] > 2012) & (Fac_data["Year"] < 2021)]
Fac_data.drop_duplicates(subset="UT", keep="first", inplace=True)
Fac_data = Fac_data.drop(
    [
        "UT",
        "context:similar_age_3m:pct",
        "context:similar_age_journal_3m:pct",
    ],
    axis=1,
)
# Fac_data.to_excel("test_Fac.xlsx")
Fac_data_group = Fac_data.groupby(["Year"]).mean().reset_index()
Fac_data_group = Fac_data_group.rename(
    columns={
        "all_top10": "Comparable Age Only",
        "j_top10": "Comparable Age in Same Journal",
    }
)
# melt it to create correct format for grouped barchart
Fac_data_group_melt = pd.melt(
    Fac_data_group,
    id_vars="Year",
    value_vars=list(Fac_data_group.columns[1:]),
    var_name="Context_type",
    value_name="Prop_90_pct",
)

# print(Fac_data_group_melt.head(16))

Fac_data_group_melt["Percent"] = Fac_data_group_melt["Prop_90_pct"] * 100
# print(Fac_data_group_melt.head(16))

####### Fellows

# get percentile data for all
Fell_alt_data_all = Fell_alt_data[["UT", "Year", "context:similar_age_3m:pct"]]
Fell_alt_data_all = Fell_alt_data_all.replace("", np.nan)
Fell_alt_data_all = Fell_alt_data_all.dropna(axis=0)
Fell_alt_data_all["all_top10"] = Fell_alt_data_all["context:similar_age_3m:pct"] >= 90
Fell_alt_data_all["all_top10"] = Fell_alt_data_all["all_top10"].astype(str)
Fell_alt_data_all["all_top10"] = Fell_alt_data_all["all_top10"].replace("True", 1)
Fell_alt_data_all["all_top10"] = Fell_alt_data_all["all_top10"].replace("False", 0)
# percentile data for journal
Fell_alt_data_j = Fell_alt_data[["UT", "Year", "context:similar_age_journal_3m:pct"]]
Fell_alt_data_j = Fell_alt_data_j.replace("", np.nan)
Fell_alt_data_j = Fell_alt_data_j.dropna(axis=0)
Fell_alt_data_j["j_top10"] = Fell_alt_data_j["context:similar_age_journal_3m:pct"] >= 90
Fell_alt_data_j["j_top10"] = Fell_alt_data_j["j_top10"].astype(str)
Fell_alt_data_j["j_top10"] = Fell_alt_data_j["j_top10"].replace("True", 1)
Fell_alt_data_j["j_top10"] = Fell_alt_data_j["j_top10"].replace("False", 0)
# merge the two together based on UT and year
Fell_data = pd.merge(
    Fell_alt_data_all,
    Fell_alt_data_j,
    on=["UT", "Year"],
)
Fell_data = Fell_data[(Fell_data["Year"] > 2013) & (Fell_data["Year"] < 2021)]
Fell_data.drop_duplicates(subset="UT", keep="first", inplace=True)
Fell_data = Fell_data.drop(
    [
        "UT",
        "context:similar_age_3m:pct",
        "context:similar_age_journal_3m:pct",
    ],
    axis=1,
)
# Fell_data.to_excel("test_Fell.xlsx")
Fell_data_group = Fell_data.groupby(["Year"]).mean().reset_index()
Fell_data_group = Fell_data_group.rename(
    columns={
        "all_top10": "Comparable Age Only",
        "j_top10": "Comparable Age in Same Journal",
    }
)
# melt it to create correct format for grouped barchart
Fell_data_group_melt = pd.melt(
    Fell_data_group,
    id_vars="Year",
    value_vars=list(Fell_data_group.columns[1:]),
    var_name="Context_type",
    value_name="Prop_90_pct",
)
Fell_data_group_melt["Percent"] = Fell_data_group_melt["Prop_90_pct"] * 100
# print(Fell_data_group_melt.head(16))
