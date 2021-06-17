import csv
import pandas as pd

VOS_twentycopubs = pd.read_csv(
    "Data/over20copubsmap.txt",
    sep="\t",
    #    engine="c",
)

VOS_twentycopubs["label"] = VOS_twentycopubs["label"].str.title()
# title format for labels helps format and thesaurus eradicates some errors (stage before this) in VOS viewer
# Need manual text edits for some labels
# print(VOS_twentycopubs["label"].head(60))
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Academy Of Sciences Of The Czech Republic",
    "Academy of Sciences Of The Czech Republic",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Boston Children'S Hospital", "Boston Children's Hospital"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Centre For Research & Technology - Hellas",
    "Centre for Research & Technology - Hellas",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Chalmers University Of Technology", "Chalmers University of Technology"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Chinese Academy Of Sciences", "Chinese Academy of Sciences"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "European Molecular Biology Laboratory (Embl)",
    "European Molecular Biology Laboratory (EMBL)",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "European Synchrotron Radiation Facility (Esrf)",
    "European Synchrotron Radiation Facility (ESRF)",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Irccs Ospedale San Raffaele", "IRCCS Ospedale San Raffaele"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Karolinska Institutet", "Karolinska Institute"
)
VOS_twentycopubs = VOS_twentycopubs.replace("Astrazeneca", "AstraZeneca")
VOS_twentycopubs = VOS_twentycopubs.replace(
    "King'S College London", "King's College London"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Kth Royal Institute Of Technology", "KTH Royal Institute of Technology"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Ludwig Maximilian University Of Munich", "Ludwig Maximilian University of Munich"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Massachusetts Institute Of Technology", "Massachusetts Institute of Technology"
)
VOS_twentycopubs = VOS_twentycopubs.replace("Mcgill University", "McGill University")
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Mrc Laboratory Of Molecular Biology (Lmb)", "MRC Laboratory of Molecular Biology"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Medical University Of Vienna", "Medical University of Vienna"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "National Public Health Institute Of Finland",
    "National Public Health Institute of Finland",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Pierre And Marie Curie University", "Pierre and Marie Curie University"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Russian Academy Of Sciences", "Russian Academy of Sciences"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Swedish University Of Agricultural Sciences",
    "Swedish University of Agricultural Sciences",
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Technical University Of Denmark", "Technical University of Denmark"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "Technical University Of Munich", "Technical University of Munich"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Barcelona", "University of Barcelona"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Basel", "University of Basel"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of California San Diego", "University of California, San Diego"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of California San Francisco", "University of California, San Francisco"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Bergen", "University of Bergen"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Cambridge", "University of Cambridge"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Copenhagen", "University of Copenhagen"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Eastern Finland", "University of Eastern Finland"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Edinburgh", "University of Edinburgh"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Gothenburg", "University of Gothenburg"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Groningen", "University of Groningen"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Helsinki", "University of Helsinki"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Liverpool", "University of Liverpool"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Manchester", "University of Manchester"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Minnesota", "University of Minnesota"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of North Carolina At Chapel Hill",
    "University of North Carolina at Chapel Hill",
)
VOS_twentycopubs = VOS_twentycopubs.replace("University Of Oslo", "University of Oslo")
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Oxford", "University of Oxford"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Tartu", "University of Tartu"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Toronto", "University of Toronto"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Washington", "University of Washington"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Zurich", "University of Zurich"
)
VOS_twentycopubs = VOS_twentycopubs.replace(
    "University Of Kwazulu-Natal", "University of Kwazulu-Natal"
)
VOS_twentycopubs = VOS_twentycopubs.replace("Eth Zurich", "ETH Zurich")
VOS_twentycopubs = VOS_twentycopubs.replace("Scilifelab", "SciLifeLab")
# print(VOS_twentycopubs["label"].head(60))
VOS_twentycopubs["score<Avg. citations>"] = (
    VOS_twentycopubs["score<Avg. citations>"] / 100
)

# write out to put back to VOS
VOS_twentycopubs.to_csv("Data/over20copubsmap_edited.txt", sep="\t", index=False)
