"""Converts first letter in strings to uppercase
script designed to work for VOS viewer files"""

import pandas as pd
import numpy as np

df = pd.read_csv(
    "/Users/liahu895/Documents/VOSviewer_1/data/testorgmap_withthes.txt", delimiter="\t"
)

df["label"] = df["label"].str.title()

df.to_csv(
    "/Users/liahu895/Documents/VOSviewer_1/data/testorgmap_withthesmod.txt",
    index=None,
    sep="\t",
)
