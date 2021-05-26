import pandas as pd

# get data from abstracts
# abstracts

##### data for fellows publications

Fellows_data = pd.read_excel(
    "Data/SciLifeLab-fellows-20210512.xlsx",
    sheet_name="publ_info",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# input the years that you're considering (IAB 2021 - 2019 and 2020)
year1 = 2019
year2 = 2020

# Need data from last 2 years for overall wordcloud
Fellows_data_range = Fellows_data[
    (Fellows_data["Publication_year"] > (year1 - 1))
    & (Fellows_data["Publication_year"] < (year2 + 1))
]
# Then also need just 2019 and 2020 (each year separately)
Fellows_data_year1 = Fellows_data[(Fellows_data["Publication_year"] == year1)]
Fellows_data_year2 = Fellows_data[(Fellows_data["Publication_year"] == year2)]

abstract_words_fell_range = ""
abstract_words_fell_year1 = ""
abstract_words_fell_year2 = ""

# pick the column you want to import words from df.columnname
# fellows abstract for date range and invidiual years
for val in Fellows_data_range.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fell_range += " ".join(tokens) + " "
for val in Fellows_data_year1.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fell_year1 += " ".join(tokens) + " "
for val in Fellows_data_year2.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fell_year2 += " ".join(tokens) + " "

##### data for facilities/units publications

Facilities_data = pd.read_excel(
    "Data/SciLifeLab-facilities-20210512.xlsx",
    sheet_name="publ_data",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# Need data from last 2 years for overall wordcloud
Facilities_data_range = Facilities_data[
    (Facilities_data["Publication_year"] > (year1 - 1))
    & (Facilities_data["Publication_year"] < (year2 + 1))
]
# Then also need just 2019 and 2020 (each year separately)
Facilities_data_year1 = Facilities_data[(Facilities_data["Publication_year"] == year1)]
Facilities_data_year2 = Facilities_data[(Facilities_data["Publication_year"] == year2)]

abstract_words_fac_range = ""
abstract_words_fac_year1 = ""
abstract_words_fac_year2 = ""

# pick the column you want to import words from df.columnname
for val in Facilities_data_range.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fac_range += " ".join(tokens) + " "
for val in Facilities_data_year1.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fac_year1 += " ".join(tokens) + " "
for val in Facilities_data_year2.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_fac_year2 += " ".join(tokens) + " "


##### data for affiliates publications

Affiliates_data = pd.read_excel(
    "Data/SciLifeLab-byaddress-20210512.xlsx",
    sheet_name="publ_info",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# Need data from last 2 years for overall wordcloud
Affiliates_data_range = Affiliates_data[
    (Affiliates_data["Publication_year"] > (year1 - 1))
    & (Affiliates_data["Publication_year"] < (year2 + 1))
]
# Then also need just 2019 and 2020 (each year separately)
Affiliates_data_year1 = Affiliates_data[(Affiliates_data["Publication_year"] == year1)]
Affiliates_data_year2 = Affiliates_data[(Affiliates_data["Publication_year"] == year2)]

abstract_words_aff_range = ""
abstract_words_aff_year1 = ""
abstract_words_aff_year2 = ""

# pick the column you want to import words from df.columnname
for val in Affiliates_data_range.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_aff_range += " ".join(tokens) + " "
for val in Affiliates_data_year1.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_aff_year1 += " ".join(tokens) + " "
for val in Affiliates_data_year2.Abstract:
    val = str(val)
    tokens = val.split()
    abstract_words_aff_year2 += " ".join(tokens) + " "