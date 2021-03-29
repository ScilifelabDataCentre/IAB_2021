""" Script will produce network file for VOS viewer"""

import pandas as pd
import networkx as nx
from itertools import combinations

# data - organisations
dforg = pd.read_excel(
    "/Users/liahu895/Documents/VOSviewer_1/testcreatingvis/SciLifeLab-byaddress-20210108.xlsx",
    sheet_name="organizations",
    engine="openpyxl",
)

# data - publications
dfpub = pd.read_excel(
    "/Users/liahu895/Documents/VOSviewer_1/testcreatingvis/SciLifeLab-byaddress-20210108.xlsx",
    sheet_name="publ_data",
    engine="openpyxl",
)

dfpubyr = dfpub[(dfpub["Publication_year"] > 2018) & (dfpub["Publication_year"] < 2021)]

# keep cols of interest for orgs
dforgsub = dforg[["UT", "Name_eng"]]

# group such that all unique affitiations associated with a UT are together
dforgsub = dforgsub.groupby("UT").agg(lambda x: ",".join(x.unique())).reset_index()

# combine list of orgs with the filtered publication list, joining on UT (get just years of interest)
mergeUT = pd.merge(dfpubyr, dforgsub, how="left", on=["UT"])

# set up for word cooccurence matrix
institutions = mergeUT["Name_eng"].str.split(",")
institutions = institutions.tolist()
# list of all institutes to be considered
labels = dforg["Name_eng"].unique()  # .tolist()
labels.to_excel("/Users/liahu895/Documents/VOSviewer_1/testcreatingvis/testnames.xlsx")


# produce data matrix
G = nx.MultiGraph()
G = nx.from_edgelist(
    (c for n_nodes in institutions for c in combinations(n_nodes, r=2)),
    create_using=nx.MultiGraph,
)
G = nx.to_pandas_adjacency(G, nodelist=labels, dtype="int")
matrix = G.to_numpy()
