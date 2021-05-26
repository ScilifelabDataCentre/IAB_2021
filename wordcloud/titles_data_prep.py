import pandas as pd

# get data from titles
# use publications database for fellows and facilities to maximise numbers
# use affiliates data from KTH for affiliates

##### data for fellows publications

Fellows_data = pd.read_excel(
    "Data/Fellows_20210419.xlsx",
    sheet_name="Publications",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)

# input the years that you're considering (IAB 2021 - 2019 and 2020)
year1 = 2019
year2 = 2020

# Need data from last 2 years for overall wordcloud
Fellows_data_range = Fellows_data[
    (Fellows_data["Year"] > (year1 - 1)) & (Fellows_data["Year"] < (year2 + 1))
]
# Then also need just 2019 and 2020 (each year separately)
Fellows_data_year1 = Fellows_data[(Fellows_data["Year"] == year1)]
Fellows_data_year2 = Fellows_data[(Fellows_data["Year"] == year2)]

title_words_fell_range = ""
title_words_fell_year1 = ""
title_words_fell_year2 = ""

# pick the column you want to import words from df.columnname
# fellows title for date range and invidiual years
for val in Fellows_data_range.Title:
    val = str(val)
    tokens = val.split()
    title_words_fell_range += " ".join(tokens) + " "
for val in Fellows_data_year1.Title:
    val = str(val)
    tokens = val.split()
    title_words_fell_year1 += " ".join(tokens) + " "
for val in Fellows_data_year2.Title:
    val = str(val)
    tokens = val.split()
    title_words_fell_year2 += " ".join(tokens) + " "

##### data for facilities/units publications

Facilities_data = pd.read_excel(
    "Data/Facilities_20210419.xlsx",
    sheet_name="Sheet1",
    header=0,
    engine="openpyxl",
    keep_default_na=False,
)


# Need data from last 2 years for overall wordcloud
Facilities_data_range = Facilities_data[
    (Facilities_data["Year"] > (year1 - 1)) & (Facilities_data["Year"] < (year2 + 1))
]
# Then also need just 2019 and 2020 (each year separately)
Facilities_data_year1 = Facilities_data[(Facilities_data["Year"] == year1)]
Facilities_data_year2 = Facilities_data[(Facilities_data["Year"] == year2)]

title_words_fac_range = ""
title_words_fac_year1 = ""
title_words_fac_year2 = ""

# pick the column you want to import words from df.columnname
# fellows title for date range and invidiual years
for val in Facilities_data_range.Title:
    val = str(val)
    tokens = val.split()
    title_words_fac_range += " ".join(tokens) + " "
for val in Facilities_data_year1.Title:
    val = str(val)
    tokens = val.split()
    title_words_fac_year1 += " ".join(tokens) + " "
for val in Facilities_data_year2.Title:
    val = str(val)
    tokens = val.split()
    title_words_fac_year2 += " ".join(tokens) + " "


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

title_words_aff_range = ""
title_words_aff_year1 = ""
title_words_aff_year2 = ""

# pick the column you want to import words from df.columnname
# fellows title for date range and invidiual years
for val in Affiliates_data_range.Title:
    val = str(val)
    tokens = val.split()
    title_words_aff_range += " ".join(tokens) + " "
for val in Affiliates_data_year1.Title:
    val = str(val)
    tokens = val.split()
    title_words_aff_year1 += " ".join(tokens) + " "
for val in Affiliates_data_year2.Title:
    val = str(val)
    tokens = val.split()
    title_words_aff_year2 += " ".join(tokens) + " "
