import pandas as pd
import numpy as np


### FAC MAP
# to their labels in the publication database
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
fac_map_input1 = fac_map_input.replace("Mass Cytometry (LiU)", "Mass Cytometry")
fac_map_input2 = fac_map_input1.replace(
    "High Throughput Genome Engineering ", "High-throughput Genome Engineering "
)
fac_map_input = fac_map_input2.replace(
    "Drug Discovery and Development ", "Drug Discovery and Development (DDD)"
)

fac_map = dict(zip(fac_map_input.Label, fac_map_input.Unit))
# print(fac_map)
df = pd.read_excel(
    "Data/Pub_19and20_oriext20210415.xlsx", sheet_name="Publications", engine="openpyxl"
)

# extract unit labels from the excel
# df["Labels"] = df["Labels"].str.replace(r"\(.*\)", "", regex=True)
df = df.replace(fac_map, regex=True)
# need to do some manual changes given that labels are combined
# This is because some labels were deleted when the publication label ends in ()
# and the puctuation is replaced with str.replace(r"\(.*\)", "", regex=True)
df = df.replace(
    "Drug Discovery and Development (DDD)", "Drug Discovery and Development"
)
df = df.replace(
    "Compute and Storage|Drug Discovery and Development (DDD)",
    "Compute and Storage|Drug Discovery and Development",
)
df = df.replace(
    "Compute and Storage|Chemical Biology Consortium Sweden(CBCS)|Drug Discovery and Development (DDD)",
    "Compute and Storage|Chemical Biology Consortium Sweden|Drug Discovery and Development",
)
df = df.replace(
    "Drug Discovery and Development (DDD)|Translational Plasma Profiling",
    "Drug Discovery and Development|Translational Plasma Profiling",
)
df = df.replace(
    "Chemical Biology Consortium Sweden(CBCS)",
    "Chemical Biology Consortium Sweden",
)
df = df.replace(
    "Chemical Biology Consortium Sweden(CBCS)|Swedish NMR Centre(SNC)",
    "Chemical Biology Consortium Sweden|Swedish NMR Centre",
)
df = df.replace(
    "Chemical Biology Consortium Sweden(CBCS)|National Genomics Infrastructure",
    "Chemical Biology Consortium Sweden|National Genomics Infrastructure",
)
df = df.replace(
    "Chemical Biology Consortium Sweden(CBCS)|Swedish Metabolomics Centre(SMC)",
    "Chemical Biology Consortium Sweden|Swedish Metabolomics Centre",
)
df = df.replace(
    "Cell Profiling|Chemical Biology Consortium Sweden(CBCS)",
    "Cell Profiling|Chemical Biology Consortium Sweden",
)
df = df.replace(
    "Swedish Metabolomics Centre(SMC)",
    "Swedish Metabolomics Centre",
)
df = df.replace(
    "Compute and Storage|Swedish Metabolomics Centre(SMC)",
    "Compute and Storage|Swedish Metabolomics Centre",
)
df = df.replace(
    "Swedish Metabolomics Centre(SMC)|Swedish NMR Centre(SNC)",
    "Swedish Metabolomics Centre|Swedish NMR Centre",
)
df = df.replace(
    "Autoimmunity and Serology Profiling|Compute and Storage|Long-term Support (WABI)|Mass Cytometry|Swedish Metabolomics Centre(SMC)|Translational Plasma Profiling",
    "Autoimmunity and Serology Profiling|Compute and Storage|Long-term Support (WABI)|Mass Cytometry|Swedish Metabolomics Centre|Translational Plasma Profiling",
)
df = df.replace(
    "Compute and Storage|National Genomics Infrastructure|Swedish Metabolomics Centre(SMC)",
    "Compute and Storage|National Genomics Infrastructure|Swedish Metabolomics Centre",
)
df = df.replace(
    "Compute and Storage|Swedish NMR Centre(SNC)",
    "Compute and Storage|Swedish NMR Centre",
)
df = df.replace(
    "Swedish NMR Centre(SNC)",
    "Swedish NMR Centre",
)
df = df.replace(
    "Eukaryotic Single Cell Genomics(ESCG)",
    "Eukaryotic Single Cell Genomics",
)
df = df.replace(
    "Compute and Storage|Eukaryotic Single Cell Genomics(ESCG)",
    "Compute and Storage|Eukaryotic Single Cell Genomics",
)
df = df.replace(
    "Compute and Storage|Eukaryotic Single Cell Genomics(ESCG)|In Situ Sequencing(ISS)|National Genomics Infrastructure",
    "Compute and Storage|Eukaryotic Single Cell Genomics|In Situ Sequencing|National Genomics Infrastructure",
)
df = df.replace(
    "Advanced Light Microscopy(ALM)|Eukaryotic Single Cell Genomics(ESCG)",
    "Advanced Light Microscopy|Eukaryotic Single Cell Genomics",
)
df = df.replace(
    "Compute and Storage|Eukaryotic Single Cell Genomics(ESCG)|National Genomics Infrastructure",
    "Compute and Storage|Eukaryotic Single Cell Genomics|National Genomics Infrastructure",
)
df = df.replace(
    "Compute and Storage|Long-term Support (WABI)|Eukaryotic Single Cell Genomics(ESCG)|In Situ Sequencing(ISS)|National Genomics Infrastructure",
    "Compute and Storage|Long-term Support (WABI)|Eukaryotic Single Cell Genomics|In Situ Sequencing|National Genomics Infrastructure",
)
df = df.replace(
    "Eukaryotic Single Cell Genomics(ESCG)|National Genomics Infrastructure",
    "Eukaryotic Single Cell Genomics|National Genomics Infrastructure",
)
df = df.replace(
    "Eukaryotic Single Cell Genomics(ESCG)|In Situ Sequencing(ISS)|National Genomics Infrastructure",
    "Eukaryotic Single Cell Genomics|In Situ Sequencing|National Genomics Infrastructure",
)
df = df.replace(
    "Eukaryotic Single Cell Genomics(ESCG)|National Genomics Infrastructure",
    "Eukaryotic Single Cell Genomics|National Genomics Infrastructure",
)
df = df.replace(
    "Compute and Storage|Long-term Support (WABI)|Support and Infrastructure|Eukaryotic Single Cell Genomics(ESCG)",
    "Compute and Storage|Long-term Support (WABI)|Support and Infrastructure|Eukaryotic Single Cell Genomics",
)
df = df.replace(
    "Compute and Storage|Long-term Support (WABI)|Eukaryotic Single Cell Genomics(ESCG)|National Genomics Infrastructure",
    "Compute and Storage|Long-term Support (WABI)|Eukaryotic Single Cell Genomics|National Genomics Infrastructure",
)
df = df.replace(
    "Compute and Storage|In Situ Sequencing(ISS)",
    "Compute and Storage|In Situ Sequencing",
)
df = df.replace(
    "In Situ Sequencing(ISS)",
    "In Situ Sequencing",
)
df = df.replace(
    "Compute and Storage|Long-term Support (WABI)|In Situ Sequencing(ISS)",
    "Compute and Storage|Long-term Support (WABI)|In Situ Sequencing",
)
df = df.replace(
    "Advanced Light Microscopy(ALM)",
    "Advanced Light Microscopy",
)
df = df.replace(
    "Advanced Light Microscopy(ALM)|Compute and Storage",
    "Advanced Light Microscopy|Compute and Storage",
)
df = df.replace(
    "Advanced Light Microscopy(ALM)|Compute and Storage|Long-term Support (WABI)|Proteogenomics",
    "Advanced Light Microscopy|Compute and Storage|Long-term Support (WABI)|Proteogenomics",
)
df = df.replace(
    "Advanced Light Microscopy(ALM)|Compute and Storage|Proteogenomics",
    "Advanced Light Microscopy|Compute and Storage|Proteogenomics",
)
df = df.replace(
    "Cryo-EM|Swedish NMR Centre(SNC)",
    "Cryo-EM|Swedish NMR Centre",
)
df = df.replace(
    "Compute and Storage|High Throughput Genome Engineering(HTGE)",
    "Compute and Storage|High Throughput Genome Engineering",
)
df = df.replace(
    "High Throughput Genome Engineering(HTGE)",
    "High Throughput Genome Engineering",
)
df = df.replace(
    "Compute and Storage|High Throughput Genome Engineering(HTGE)|National Genomics Infrastructure",
    "Compute and Storage|High Throughput Genome Engineering|National Genomics Infrastructure",
)
df.to_excel("test.xlsx")
