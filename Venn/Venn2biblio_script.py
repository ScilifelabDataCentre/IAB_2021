from matplotlib_venn import venn2, venn2_unweighted, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd

# This script makes a simple 2 group venn diagram
# it automatically calculates percentages and values and labels accordingly, just put in correct data
# put data for 2 groups - facilities and affiliates
# Have 2 versions for facilities extract (from pub database and from BIBMET - maximise matches by considering both as BIBMET coverage never 100%)
facilities_pub = pd.read_excel(
    "Data_venn/Facilities_20210419.xlsx", sheet_name="Sheet1", engine="openpyxl"
)
facilities_bib = pd.read_excel(
    "Data_venn/SciLifeLab-facilities-20210512.xlsx",
    sheet_name="publ_data",
    engine="openpyxl",
)
affiliates_bib = pd.read_excel(
    "Data_venn/SciLifeLab-byaddress-20210512.xlsx",
    sheet_name="publ_info",
    engine="openpyxl",
)

# For IAB 2019 used 2017 and 2018. so, will use 2019 and 2020

# facilities data requires some further processing when matching on UT.
# not all facilities publications are in BIBMET
# union between groups will be right as affiliates ONLY from BIBMET
# however, there are more publications in the facilities lists in the database
# to ensure everything is right, quicker to add some manual values

facs_bib = facilities_bib[
    (facilities_bib["Publication_year"] > 2018)
    & (facilities_bib["Publication_year"] < 2021)
]
# facs_pubdb = facilities_pub[
#     (facilities_pub["Year"] > 2018) & (facilities_pub["Year"] < 2021)
# ]

# affiliates data requires no further processing only filter for years
affs_bib = affiliates_bib[
    (affiliates_bib["Publication_year"] > 2018)
    & (affiliates_bib["Publication_year"] < 2021)
]

# # fac_set_UT = set(facs_bib["UT"])
# # aff_set_UT = set(affs_bib["UT"])
# # Make a weighted Venn - get initial values (incorrect for just facilities, but afiliates and union correct)
# # total = len(fac_set_UT.union(aff_set_UT))
# # v = venn2(
# #     subsets=[fac_set_UT, aff_set_UT],
# #     next line would set labels outside the circles
# #     set_labels=(
# #         "Unit Users",
# #         "Affliated researchers",
# #     ),
# #     set_colors=("#A7C947", "#4C979F"),
# #     subset_label_formatter=lambda x: f"{x}\n({(x/total):1.0%})",
# #     alpha=1.0,
# #     ax=plt.gca(),
# # )
# # set outer labels
# # for text in v.set_labels:
# #     text.set_fontsize(12)
# # below recolours overlapping sections to be consistent with scilifelab visual ID
# # v.get_patch_by_id("11").set_color("#a48fa9")
# # plt.show()

# now read values from the plot shown
# IAB 2021 - 463 in union, 1166 in aff
# Previous calculations (see JIF plots and raw facilities extract) suggest there are in total 1218 facility publications
# However, original venn calculation above suggests 1121 (463 + 658), so should actually see 97 more publications for just facilities (755)
# quickest for me to add these manually

inoverlap = 463
facilityonly = 755
affiliateonly = 1166

real_total = inoverlap + facilityonly + affiliateonly

percover = round((inoverlap / real_total) * 100)
percfac = round((facilityonly / real_total) * 100)
percaff = round((affiliateonly / real_total) * 100)


v_use = venn2(
    subsets=(percfac, percaff, percover),
    # next line would set labels outside the circles
    set_labels=(
        "Unit Users",
        "Affliated researchers",
    ),
    set_colors=("#A7C947", "#4C979F"),
    alpha=1.0,
    ax=plt.gca(),
)
v_use.get_label_by_id("01").set_text("{}\n({}%)".format(affiliateonly, percaff))
v_use.get_label_by_id("10").set_text("{}\n({}%)".format(facilityonly, percfac))
v_use.get_label_by_id("11").set_text("{}\n({}%)".format(inoverlap, percover))
# set outer labels
for text in v_use.set_labels:
    text.set_fontsize(12)
# # below recolours overlapping sections to be consistent with scilifelab visual ID
v_use.get_patch_by_id("11").set_color("#a48fa9")
# plt.show()
# #Uncomment the above to show the figure, the below saves the figure, but a blank image will be saved if plt.show() is done first
plt.savefig("Venn_affiliates_and_fellows.svg", dpi=300)
