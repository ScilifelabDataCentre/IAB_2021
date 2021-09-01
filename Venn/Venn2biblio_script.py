from matplotlib_venn import venn2, venn2_unweighted, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd

# This script makes a simple 2 group venn diagram
# Information on n and % of publications is calculated automatically.
# put data for 2 groups - facilities and affiliates

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

# IAB report uses last 2 years (e.g. IAB 2021: use 2019 and 2020)

# IMPORTANT! There are two sources of data for facilities publications; our database and the data extracts.
# Coverage is not 100% in searches but numbers must align for facilities. This requires some manual work.

# Load the data from extracts
facs_bib = facilities_bib[
    (facilities_bib["Publication_year"] > 2018)
    & (facilities_bib["Publication_year"] < 2021)
]

affs_bib = affiliates_bib[
    (affiliates_bib["Publication_year"] > 2018)
    & (affiliates_bib["Publication_year"] < 2021)
]

# uncomment the below section of script - examine the values when matching based on UT.
# The values will be correct for affiliates and the intersect, but not for facilities. You need to examine the total number for infrastructure and add the missing amount

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

# now you can use the below to produce a graph with the correct values manually inserted.
# the below values are true for IAB 2021 report.

inoverlap = 463
facilityonly = 755
affiliateonly = 1166

real_total = inoverlap + facilityonly + affiliateonly

percover = round((inoverlap / real_total) * 100)
percfac = round((facilityonly / real_total) * 100)
percaff = round((affiliateonly / real_total) * 100)


v_use = venn2(
    subsets=(percfac, percaff, percover),
    # set labels outside of circles
    set_labels=(
        "Infrastructure Users",
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
    text.set_fontsize(16)
for text in v_use.subset_labels:
    text.set_fontsize(20)
# # below recolours overlapping sections to be consistent with scilifelab visual ID
v_use.get_patch_by_id("11").set_color("#a48fa9")
# plt.show()
# Uncomment the above to show the figure - useful for tests, the below saves the figure, but a blank image will be saved if plt.show() is not commented out
plt.savefig("Venn_affiliates_and_fellows_v2.svg", dpi=300)
plt.savefig("Venn_affiliates_and_fellows_v2.png", dpi=300)
