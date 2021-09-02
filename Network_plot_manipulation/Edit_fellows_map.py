import csv
import pandas as pd

VOS_SLL = pd.read_csv(
    "Data/UPDATE_FELLOWS_map_201518.txt",
    sep="\t",
    #    engine="c",
)

VOS_SLL["label"] = VOS_SLL["label"].str.title()
# title format for labels helps format and thesaurus eradicates some errors (stage before this) in VOS viewer
# print(VOS_SLL.head(30)) check labels and what edits needed
# Need manual text edits for some labels
VOS_SLL = VOS_SLL.replace(
    "Barcelona Institute Of Science And Technology",
    "Barcelona Institute of Science and Technology",
)
VOS_SLL = VOS_SLL.replace("Dsm Nutr Prod Ltd", "DSM Nutritional Products Ltd")
VOS_SLL = VOS_SLL.replace("Boston Children'S Hospital", "Boston Children's Hospital")
VOS_SLL = VOS_SLL.replace(
    "Centre For Research & Technology - Hellas",
    "Centre for Research & Technology - Hellas",
)
VOS_SLL = VOS_SLL.replace(
    "Chalmers University Of Technology", "Chalmers University of Technology"
)
VOS_SLL = VOS_SLL.replace(
    "European Bioinformatics Institute (Embl-Ebi)",
    "European Bioinformatics Institute (EMBL-EBI)",
)
VOS_SLL = VOS_SLL.replace(
    "Leibniz Institute Of Freshwater Ecology And Inland Fisheries (Igb)",
    "IGB-Leibniz",
)
VOS_SLL = VOS_SLL.replace(
    "French National Centre For Scientific Research",
    "French National Centre for Scientific Research",
)
VOS_SLL = VOS_SLL.replace(
    "Russian Academy Of Sciences",
    "Russian Academy of Sciences",
)
VOS_SLL = VOS_SLL.replace(
    "National Institutes Of Health",
    "National Institutes of Health (NIH)",
)
VOS_SLL = VOS_SLL.replace(
    "Mrc Laboratory Of Molecular Biology (Lmb)",
    "MRC Laboratory of Molecular Biology",
)
VOS_SLL = VOS_SLL.replace(
    "European Molecular Biology Laboratory (Embl)",
    "European Molecular Biology Laboratory (EMBL)",
)
VOS_SLL = VOS_SLL.replace("General Hospital Of Nikea", "General Hospital of Nikea")
VOS_SLL = VOS_SLL.replace(
    "George Papanikolaou General Hospital Of Thessaloniki",
    "George Papanikolaou General Hospital of Thessaloniki",
)
VOS_SLL = VOS_SLL.replace(
    "Icahn School Of Medicine At Mount Sinai", "Icahn School of Medicine at Mount Sinai"
)
VOS_SLL = VOS_SLL.replace("Irccs Ospedale San Raffaele", "IRCCS Ospedale San Raffaele")
VOS_SLL = VOS_SLL.replace("Karolinska Institutet", "Karolinska Institute")
VOS_SLL = VOS_SLL.replace("Astrazeneca", "AstraZeneca")
VOS_SLL = VOS_SLL.replace("King'S College London", "King's College London")
VOS_SLL = VOS_SLL.replace(
    "Kth Royal Institute Of Technology", "KTH Royal Institute of Technology"
)
VOS_SLL = VOS_SLL.replace(
    "Massachusetts Institute Of Technology", "Massachusetts Institute of Technology"
)
VOS_SLL = VOS_SLL.replace("Mcgill University", "McGill University")
VOS_SLL = VOS_SLL.replace(
    "Medical University Of Vienna", "Medical University of Vienna"
)
VOS_SLL = VOS_SLL.replace(
    "National And Kapodistrian University Of Athens",
    "National and Kapodistrian University of Athens",
)
VOS_SLL = VOS_SLL.replace(
    "National Public Health Institute Of Finland",
    "National Public Health Institute of Finland",
)
VOS_SLL = VOS_SLL.replace(
    "Norwegian University Of Science And Technology",
    "Norwegian University of Science and Technology",
)
VOS_SLL = VOS_SLL.replace(
    "Pierre And Marie Curie University", "Pierre and Marie Curie University"
)
VOS_SLL = VOS_SLL.replace(
    "Queen Mary University Of London", "Queen Mary University of London"
)
VOS_SLL = VOS_SLL.replace(
    "Swedish University Of Agricultural Sciences",
    "Swedish University of Agricultural Sciences",
)
VOS_SLL = VOS_SLL.replace(
    "Swiss Institute Of Bioinformatics", "Swiss Institute of Bioinformatics"
)
VOS_SLL = VOS_SLL.replace(
    "Technical University Of Denmark", "Technical University of Denmark"
)
VOS_SLL = VOS_SLL.replace(
    "Technical University Of Munich", "Technical University of Munich"
)
VOS_SLL = VOS_SLL.replace("Univ Hosp Brno", "University Hospital Brno")
VOS_SLL = VOS_SLL.replace("University Of Barcelona", "University of Barcelona")
VOS_SLL = VOS_SLL.replace("University Of Basel", "University of Basel")
VOS_SLL = VOS_SLL.replace("University Of Bonn", "University of Bonn")
VOS_SLL = VOS_SLL.replace(
    "University Of British Columbia", "University of British Columbia"
)
VOS_SLL = VOS_SLL.replace(
    "University Of California San Diego", "University of California, San Diego"
)
VOS_SLL = VOS_SLL.replace(
    "University Of California San Francisco", "University of California, San Francisco"
)
VOS_SLL = VOS_SLL.replace(
    "University Of California, Berkeley", "University of California, Berkeley"
)
VOS_SLL = VOS_SLL.replace("University Of Cambridge", "University of Cambridge")
VOS_SLL = VOS_SLL.replace("University Of Pennsylvania", "University of Pennsylvania")
VOS_SLL = VOS_SLL.replace("University Of Copenhagen", "University of Copenhagen")
VOS_SLL = VOS_SLL.replace(
    "University Of Eastern Finland", "University of Eastern Finland"
)
VOS_SLL = VOS_SLL.replace("University Of Valencia", "University of Valencia")
VOS_SLL = VOS_SLL.replace(
    "University Of Wisconsin–Stevens Point (Uwsp)",
    "University of Wisconsin–Stevens Point",
)
VOS_SLL = VOS_SLL.replace("University Of Edinburgh", "University of Edinburgh")
VOS_SLL = VOS_SLL.replace("University Of Geneva", "University of Geneva")
VOS_SLL = VOS_SLL.replace("University Of Gothenburg", "University of Gothenburg")
VOS_SLL = VOS_SLL.replace("University Of Groningen", "University of Groningen")
VOS_SLL = VOS_SLL.replace("University Of Helsinki", "University of Helsinki")
VOS_SLL = VOS_SLL.replace("University Of Jena", "University of Jena")
VOS_SLL = VOS_SLL.replace("University Of Montpellier", "University of Montpellier")
VOS_SLL = VOS_SLL.replace("University Of Montreal", "University of Montreal")
VOS_SLL = VOS_SLL.replace("University Of Jyvaskyla", "University of Jyvaskyla")
VOS_SLL = VOS_SLL.replace("University Of Liverpool", "University of Liverpool")
VOS_SLL = VOS_SLL.replace("University Of Manchester", "University of Manchester")
VOS_SLL = VOS_SLL.replace("University Of Michigan", "University of Michigan")
VOS_SLL = VOS_SLL.replace("University Of Minnesota", "University of Minnesota")
VOS_SLL = VOS_SLL.replace(
    "University Of North Carolina At Chapel Hill",
    "University of North Carolina at Chapel Hill",
)
VOS_SLL = VOS_SLL.replace("University Of Oslo", "University of Oslo")
VOS_SLL = VOS_SLL.replace("University Of Oulu", "University of Oulu")
VOS_SLL = VOS_SLL.replace("University Of Oxford", "University of Oxford")
VOS_SLL = VOS_SLL.replace("University Of Padova", "University of Padova")
VOS_SLL = VOS_SLL.replace("University Of Queensland", "University of Queensland")
VOS_SLL = VOS_SLL.replace("University Of Southampton", "University of Southampton")
VOS_SLL = VOS_SLL.replace("University Of Tartu", "University of Tartu")
VOS_SLL = VOS_SLL.replace("University Of Toronto", "University of Toronto")
VOS_SLL = VOS_SLL.replace("University Of Turku", "University of Turku")
VOS_SLL = VOS_SLL.replace("University Of Washington", "University of Washington")
VOS_SLL = VOS_SLL.replace("University Of Zurich", "University of Zurich")
VOS_SLL = VOS_SLL.replace("Biomeditech", "BioMediTech")
VOS_SLL = VOS_SLL.replace("Eth Zurich", "ETH Zurich")
VOS_SLL = VOS_SLL.replace("Scilifelab", "SciLifeLab")
VOS_SLL["score<Avg. citations>"] = VOS_SLL["score<Avg. citations>"] / 100

# write out to put back to VOS
VOS_SLL.to_csv("Data/UPDATE_FELLOWS_map_201518_edited.txt", sep="\t", index=False)
