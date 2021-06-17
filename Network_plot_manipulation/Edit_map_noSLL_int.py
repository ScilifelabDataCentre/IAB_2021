import csv
import pandas as pd

VOS_noSLL = pd.read_csv(
    "Data/tophundred_noSLL.txt",
    sep="\t",
    #    engine="c",
)

VOS_noSLL["label"] = VOS_noSLL["label"].str.title()
# title format for labels helps format and thesaurus eradicates some errors (stage before this) in VOS viewer
# print(VOS_noSLL.head(30)) check labels and what edits needed
# Need manual text edits for some labels
VOS_noSLL = VOS_noSLL.replace(
    "Barcelona Institute Of Science And Technology",
    "Barcelona Institute of Science and Technology",
)
VOS_noSLL = VOS_noSLL.replace(
    "Boston Children'S Hospital", "Boston Children's Hospital"
)
VOS_noSLL = VOS_noSLL.replace(
    "Centre For Research & Technology - Hellas",
    "Centre for Research & Technology - Hellas",
)
VOS_noSLL = VOS_noSLL.replace(
    "Chalmers University Of Technology", "Chalmers University of Technology"
)
VOS_noSLL = VOS_noSLL.replace(
    "European Bioinformatics Institute (Embl-Ebi)",
    "European Bioinformatics Institute (EMBL-EBI)",
)
VOS_noSLL = VOS_noSLL.replace(
    "European Molecular Biology Laboratory (Embl)",
    "European Molecular Biology Laboratory (EMBL)",
)
VOS_noSLL = VOS_noSLL.replace("General Hospital Of Nikea", "General Hospital of Nikea")
VOS_noSLL = VOS_noSLL.replace(
    "George Papanikolaou General Hospital Of Thessaloniki",
    "George Papanikolaou General Hospital of Thessaloniki",
)
VOS_noSLL = VOS_noSLL.replace(
    "Icahn School Of Medicine At Mount Sinai", "Icahn School of Medicine at Mount Sinai"
)
VOS_noSLL = VOS_noSLL.replace(
    "Irccs Ospedale San Raffaele", "IRCCS Ospedale San Raffaele"
)
VOS_noSLL = VOS_noSLL.replace("Karolinska Institutet", "Karolinska Institute")
VOS_noSLL = VOS_noSLL.replace("Astrazeneca", "AstraZeneca")
VOS_noSLL = VOS_noSLL.replace("King'S College London", "King's College London")
VOS_noSLL = VOS_noSLL.replace(
    "Kth Royal Institute Of Technology", "KTH Royal Institute of Technology"
)
VOS_noSLL = VOS_noSLL.replace(
    "Massachusetts Institute Of Technology", "Massachusetts Institute of Technology"
)
VOS_noSLL = VOS_noSLL.replace("Mcgill University", "McGill University")
VOS_noSLL = VOS_noSLL.replace(
    "Medical University Of Vienna", "Medical University of Vienna"
)
VOS_noSLL = VOS_noSLL.replace(
    "National And Kapodistrian University Of Athens",
    "National and Kapodistrian University of Athens",
)
VOS_noSLL = VOS_noSLL.replace(
    "National Public Health Institute Of Finland",
    "National Public Health Institute of Finland",
)
VOS_noSLL = VOS_noSLL.replace(
    "Norwegian University Of Science And Technology",
    "Norwegian University of Science and Technology",
)
VOS_noSLL = VOS_noSLL.replace(
    "Pierre And Marie Curie University", "Pierre and Marie Curie University"
)
VOS_noSLL = VOS_noSLL.replace(
    "Queen Mary University Of London", "Queen Mary University of London"
)
VOS_noSLL = VOS_noSLL.replace(
    "Swedish University Of Agricultural Sciences",
    "Swedish University of Agricultural Sciences",
)
VOS_noSLL = VOS_noSLL.replace(
    "Swiss Institute Of Bioinformatics", "Swiss Institute of Bioinformatics"
)
VOS_noSLL = VOS_noSLL.replace(
    "Technical University Of Denmark", "Technical University of Denmark"
)
VOS_noSLL = VOS_noSLL.replace(
    "Technical University Of Munich", "Technical University of Munich"
)
VOS_noSLL = VOS_noSLL.replace("Univ Hosp Brno", "University Hospital Brno")
VOS_noSLL = VOS_noSLL.replace("University Of Barcelona", "University of Barcelona")
VOS_noSLL = VOS_noSLL.replace("University Of Basel", "University of Basel")
VOS_noSLL = VOS_noSLL.replace(
    "University Of California San Diego", "University of California, San Diego"
)
VOS_noSLL = VOS_noSLL.replace(
    "University Of California San Francisco", "University of California, San Francisco"
)
VOS_noSLL = VOS_noSLL.replace(
    "University Of California, Berkeley", "University of California, Berkeley"
)
VOS_noSLL = VOS_noSLL.replace("University Of Cambridge", "University of Cambridge")
VOS_noSLL = VOS_noSLL.replace("University Of Copenhagen", "University of Copenhagen")
VOS_noSLL = VOS_noSLL.replace(
    "University Of Eastern Finland", "University of Eastern Finland"
)
VOS_noSLL = VOS_noSLL.replace("University Of Edinburgh", "University of Edinburgh")
VOS_noSLL = VOS_noSLL.replace("University Of Geneva", "University of Geneva")
VOS_noSLL = VOS_noSLL.replace("University Of Gothenburg", "University of Gothenburg")
VOS_noSLL = VOS_noSLL.replace("University Of Groningen", "University of Groningen")
VOS_noSLL = VOS_noSLL.replace("University Of Helsinki", "University of Helsinki")
VOS_noSLL = VOS_noSLL.replace("University Of Liverpool", "University of Liverpool")
VOS_noSLL = VOS_noSLL.replace("University Of Manchester", "University of Manchester")
VOS_noSLL = VOS_noSLL.replace("University Of Michigan", "University of Michigan")
VOS_noSLL = VOS_noSLL.replace("University Of Minnesota", "University of Minnesota")
VOS_noSLL = VOS_noSLL.replace(
    "University Of North Carolina At Chapel Hill",
    "University of North Carolina at Chapel Hill",
)
VOS_noSLL = VOS_noSLL.replace("University Of Oslo", "University of Oslo")
VOS_noSLL = VOS_noSLL.replace("University Of Oulu", "University of Oulu")
VOS_noSLL = VOS_noSLL.replace("University Of Oxford", "University of Oxford")
VOS_noSLL = VOS_noSLL.replace("University Of Padova", "University of Padova")
VOS_noSLL = VOS_noSLL.replace("University Of Queensland", "University of Queensland")
VOS_noSLL = VOS_noSLL.replace("University Of Southampton", "University of Southampton")
VOS_noSLL = VOS_noSLL.replace("University Of Tartu", "University of Tartu")
VOS_noSLL = VOS_noSLL.replace("University Of Toronto", "University of Toronto")
VOS_noSLL = VOS_noSLL.replace("University Of Turku", "University of Turku")
VOS_noSLL = VOS_noSLL.replace("University Of Washington", "University of Washington")
VOS_noSLL = VOS_noSLL.replace("University Of Zurich", "University of Zurich")
VOS_noSLL = VOS_noSLL.replace("Biomeditech", "BioMediTech")
VOS_noSLL = VOS_noSLL.replace("Eth Zurich", "ETH Zurich")
VOS_noSLL["score<Avg. citations>"] = VOS_noSLL["score<Avg. citations>"] / 100

# write out to put back to VOS
VOS_noSLL.to_csv("Data/tophundred_noSLL_edited.txt", sep="\t", index=False)
