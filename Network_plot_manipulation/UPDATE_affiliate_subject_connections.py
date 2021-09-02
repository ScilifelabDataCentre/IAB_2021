"""produced this to consider connections between subject categories"""
import csv
import pandas as pd

VOS = pd.read_csv(
    "Data/SLL_BM20Q4_byaddress_modified.txt",
    sep="\t",
    #    engine="c",
)


VOS["PY"] = VOS["PY"].astype(int)
# years we have for impact values (from 13 in line with other analyses)
VOS_sub = VOS[(VOS["PY"] > 2014) & (VOS["PY"] < 2019)]
#
VOS_sub = VOS_sub[
    (VOS_sub["Doc_type_code_rev"] == "RV")
    | (VOS_sub["Doc_type_code_rev"] == "AR")
    | (VOS_sub["Doc_type_code_rev"] == "PP")
]
# rename mncs to TC to use it in overlayvis (TC is usually total citations, which VOS gives as default options)
VOS_sub.rename(columns={"TC": "Raw_cites", "Cf_scxwo": "TC"}, inplace=True)
VOS_sub["TC"] = VOS_sub["TC"].astype(float)
VOS_sub["TC"] = VOS_sub["TC"] * 100
VOS_sub["TC"] = VOS_sub["TC"].astype(int)
# Float values do not work well in VOS viewer - better to use int
# print(VOS_sub["TC"].head())
# have a different column to read as title
VOS_sub.rename(columns={"TI": "Raw_titles", "label_lev4": "TI"}, inplace=True)
VOS_sub["TI"] = VOS_sub["TI"].str.replace("//", "; ")
# print(VOS_sub["TI"].head())
VOS_sub.to_csv("Data/UPDATEfiltered_lev4subjectcategories.txt", sep="\t", index=False)
