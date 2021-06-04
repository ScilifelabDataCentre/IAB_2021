import pandas as pd
import numpy as np

# Focus on data for (1) - extract individual labels for records from pub db

Pubs_cat_raw = pd.read_excel(
    "Data/Pub_18to20_indivlab_20210415.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# Need to get data for (fac) and groupby


pub_sub = Pubs_cat_raw[["Year", "Labels", "Qualifiers"]]
pub_sub = pub_sub[(pub_sub["Year"] == 2020) | (pub_sub["Year"] == 2019)]
pub_sub = pub_sub.replace(r"^\s*$", "No category", regex=True)
pub_sub["Qualifiers"] = pub_sub["Qualifiers"].astype("category")

pub_cat_group = pub_sub.groupby(["Qualifiers"]).size().reset_index()

print(pub_cat_group)

# pub_cat_data_basic = pub_cat_group.replace(fac_map, regex=True)

# pub_concat_data.columns = ["Year", "Unit", "Qualifiers", "Count"]

# pub_cat_data = pub_concat_data
