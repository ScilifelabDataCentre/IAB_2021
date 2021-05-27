"""This script sorts the data for facilities for the last 2 years 
to identify just the publications that at least one facility identifies 
as involved in technology development"""
import pandas as pd
import numpy as np
from fac_map import df

techdev_df = df

techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Collaborative|",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "|Service|Collaborative|Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Service|Collaborative|Collaborative|Collaborative|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "|Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service||Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service||Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Service|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Technology development|Technology development|Service|Service",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Technology development|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Collaborative|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Service|Technology development|Service",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Service|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Technology development|Service|Technology development|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Technology development|Service",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Technology development",
    "Technology development",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Service|Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Service|Service|Collaborative|Collaborative|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|Collaborative|Service|Service",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative|Service|Collaborative",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Service|",
    "",
)
techdev_df["Qualifiers"] = techdev_df["Qualifiers"].replace(
    "Collaborative",
    "",
)

# print this out and check that everything has appropriately been replaced
# if so, then only "technology development" will appear in the Qualifiers column
# might need to add more replacements to the above to achieve this-manually check below document to be sure
techdev_df.to_excel("techdevfilteringcheck.xlsx")

techdev_df = techdev_df[(techdev_df["Qualifiers"] == "Technology development")]
