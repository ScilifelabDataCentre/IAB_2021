import csv
import pandas as pd

VOS_Swe = pd.read_csv(
    "Data/UPDATE_nat_map_201518.txt",
    sep="\t",
    #    engine="c",
)

VOS_Swe["label"] = VOS_Swe["label"].str.title()
# title format for labels helps format and thesaurus eradicates some errors (stage before this) in VOS viewer
# print(VOS_Swe.head(50))  # check labels and what edits needed
# Need manual text edits for some labels


VOS_Swe = VOS_Swe.replace(
    "Bioinformatics Infrastructure For Life Sciences",
    "Bioinformatics Infrastructure for Life Sciences",
)
VOS_Swe = VOS_Swe.replace(
    "Cellutech Ab",
    "Cellutech AB",
)
VOS_Swe = VOS_Swe.replace(
    "Chalmers University Of Technology",
    "Chalmers University of Technology",
)
VOS_Swe = VOS_Swe.replace(
    "Kth Royal Institute Of Technology",
    "KTH Royal Institute of Technology",
)
VOS_Swe = VOS_Swe.replace(
    "Linnean Centre Of Plant Biology",
    "Linnean Centre of Plant Biology",
)
VOS_Swe = VOS_Swe.replace(
    "National Board Of Forensic Medicine",
    "National Board of Forensic Medicine",
)
VOS_Swe = VOS_Swe.replace(
    "Norrland'S University Hospital",
    "Norrland's University Hospital",
)
VOS_Swe = VOS_Swe.replace(
    "Olink Proteomics Ab",
    "Olink Proteomics AB",
)
VOS_Swe = VOS_Swe.replace(
    "Public Health Agency Of Sweden",
    "Public Health Agency of Sweden",
)
VOS_Swe = VOS_Swe.replace(
    "Rise - Research Institutes Of Sweden",
    "RISE - Research Institutes of Sweden",
)
VOS_Swe = VOS_Swe.replace(
    "Scilifelab",
    "SciLifeLab",
)
VOS_Swe = VOS_Swe.replace(
    "Ssi",
    "SSI",
)
VOS_Swe = VOS_Swe.replace(
    "Ssi",
    "SSI",
)
VOS_Swe = VOS_Swe.replace(
    "Ssi",
    "SSI",
)
VOS_Swe = VOS_Swe.replace(
    "Swedish Museum Of Natural History",
    "Swedish Museum Of Natural History",
)
VOS_Swe = VOS_Swe.replace(
    "Swedish Orphan Biovitrum Ab",
    "Swedish Orphan Biovitrum AB",
)
VOS_Swe = VOS_Swe.replace(
    "Swedish University Of Agricultural Sciences",
    "Swedish University of Agricultural Sciences",
)
VOS_Swe = VOS_Swe.replace(
    "University Of Gothenburg",
    "University of Gothenburg",
)
VOS_Swe = VOS_Swe.replace(
    "Swedish Museum Of Natural History",
    "Swedish Museum of Natural History",
)
VOS_Swe["score<Avg. citations>"] = VOS_Swe["score<Avg. citations>"] / 100
# write out to put back to VOS
VOS_Swe.to_csv("Data/UPDATE_nat_map_201518_edited.txt", sep="\t", index=False)
