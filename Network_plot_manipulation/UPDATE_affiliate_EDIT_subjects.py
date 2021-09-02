import csv
import pandas as pd

VOS_Swe = pd.read_csv(
    "Data/UPDATE_subject_map_201518.txt",
    sep="\t",
    #    engine="c",
)

VOS_Swe["label"] = VOS_Swe["label"].str.title()
# title format for labels helps format and thesaurus eradicates some errors (stage before this) in VOS viewer
# print(VOS_Swe["label"][60:120])  # check labels and what edits needed
# Need manual text edits for some labels


VOS_Swe = VOS_Swe.replace(
    "Civil Engn",
    "Civil Engineering",
)
VOS_Swe = VOS_Swe.replace(
    "Education Educational Research",
    "Educational Research",
)
VOS_Swe = VOS_Swe.replace(
    "Endodontic",
    "Endodontics",
)
VOS_Swe = VOS_Swe.replace(
    "Gastroenterology Hepatology",
    "Gastroenterology & Hepatology",
)
VOS_Swe = VOS_Swe.replace(
    "Geochemistry & Geophysic",
    "Geochemistry & Geophysics",
)
VOS_Swe = VOS_Swe.replace(
    "Geophysical Research Space Physics",
    "Geophysical Research (Space Physics)",
)
VOS_Swe = VOS_Swe.replace(
    "Life Sci Informat",
    "Life Science Information",
)
VOS_Swe = VOS_Swe.replace(
    "Information System",
    "Information Systems",
)
VOS_Swe = VOS_Swe.replace(
    "Economic",
    "Economics",
)
VOS_Swe = VOS_Swe.replace(
    "Optic",
    "Optics",
)
VOS_Swe = VOS_Swe.replace(
    "Orthopaed Surg",
    "Orthopaed Surgery",
)
VOS_Swe = VOS_Swe.replace(
    "Orthopedic",
    "Orthopedics",
)
VOS_Swe = VOS_Swe.replace(
    "Rna",
    "RNA",
)
VOS_Swe = VOS_Swe.replace(
    "Tgf Beta",
    "TGF-Beta",
)
VOS_Swe = VOS_Swe.replace(
    "Trans Translation",
    "Trans-Translation",
)
VOS_Swe = VOS_Swe.replace(
    "Uracil Dna Glycosylase",
    "Uracil DNA Glycosylase",
)
VOS_Swe = VOS_Swe.replace(
    "Swedish Orphan Biovitrum Ab",
    "Swedish Orphan Biovitrum AB",
)
VOS_Swe = VOS_Swe.replace(
    "Angiotensin Ii",
    "Angiotensin II",
)
VOS_Swe = VOS_Swe.replace(
    "Beta Catenin",
    "Beta-Catenin",
)
VOS_Swe = VOS_Swe.replace(
    "Cardiol",
    "Cardiology",
)
VOS_Swe = VOS_Swe.replace(
    "Orthopaed Surgery",
    "Orthopaedic Surgery",
)
# print(VOS_Swe.head(60))
# print(VOS_Swe["label"][60:120])

VOS_Swe["score<Avg. citations>"] = VOS_Swe["score<Avg. citations>"] / 100
# write out to put back to VOS
VOS_Swe.to_csv("Data/UPDATE_subject_map_201518_edited.txt", sep="\t", index=False)
