"""Script designed to concatenate files from
publications database for required years"""

import pandas as pd

# Import years 2013-2020 (for 2021 years of interest)
fac_2013 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2013.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2014 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2014.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2015 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2015.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2016 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2016.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2017 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2017.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2018 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2018.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2019 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2019.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

fac_2020 = pd.read_excel(
    "/Users/liahu895/Documents/scilifelab/General information IAB 2021/IAB_pubdata/Raw_pub_data_to_KTH/fac_2020.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# concatenate years together
Fac_13to20 = pd.concat(
    [fac_2013, fac_2014, fac_2015, fac_2016, fac_2017, fac_2018, fac_2019, fac_2020]
)
# Write out to excel
Fac_13to20.to_excel("Facilities_20210419.xlsx")
