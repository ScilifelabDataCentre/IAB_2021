import pandas as pd
import numpy as np


### FAC MAP
# map to their labels in the publication database
fac_map_input = pd.read_excel(
    "Data/Reporting Units 2020.xlsx",
    sheet_name="Reporting units",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)
fac_map_input["PDB label"] = fac_map_input["PDB label"].str.replace(
    r"\(.*\)", "", regex=True
)
fac_map_input = fac_map_input[["Unit", "PDB label"]]
fac_map_input = fac_map_input.replace("", np.nan)
fac_map_input["PDB label"] = fac_map_input["PDB label"].fillna(fac_map_input["Unit"])
fac_map_input.rename(columns={"PDB label": "Label"}, inplace=True)
fac_map = dict(zip(fac_map_input.Label, fac_map_input.Unit))
print(fac_map)
