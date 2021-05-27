import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# already worked out total funding as tot_fund
# and facility data is uploaded from there too - can use FTEs from there - also need to log
from fundvspubs_scatter import Facility_data, tot_fund, Funding_comb
from colour_science_2020 import (
    SCILIFE_COLOURS,
)


# function to draw the individual pie markers (code modified from that found here: https://stackoverflow.com/questions/56337732/how-to-plot-scatter-pie-chart-using-matplotlib)
def drawPieMarker(xs, ys, ratios, sizes, colors):
    assert sum(ratios) <= 1, "sum of ratios needs to be < 1"

    markers = []
    previous = 0
    # calculate the points of the pie pieces
    for color, ratio in zip(colors, ratios):
        this = 2 * np.pi * ratio + previous
        x = [0] + np.cos(np.linspace(previous, this, 10)).tolist() + [0]
        y = [0] + np.sin(np.linspace(previous, this, 10)).tolist() + [0]
        xy = np.column_stack([x, y])
        previous = this
        markers.append(
            {
                "marker": xy,
                "edgecolor": "0",
                "linewidth": 1,
                "s": np.abs(xy).max() ** 2 * np.array(sizes),
                "facecolor": color,
            }
        )

    # scatter each of the pie pieces to create pies
    for marker in markers:
        ax.scatter(xs, ys, **marker)


# Get data in shape
# Need total funding logged, FTEs logged (in total)
# Asked for two versions, one with user fees included in the total, one with user fees not included in the total
# then funding split by other funds, scilifelab funding and user fees

# Think I need to add user fees too before I calculate the total actual funding
User_fees = Facility_data[["Facility", "Platform", "User Fees 2020 Total (kSEK)"]]
User_fees.insert(loc=2, column="Financier", value="User fees")
User_fees.rename(
    columns={"User Fees 2020 Total (kSEK)": "Amount (kSEK)"},
    inplace=True,
)
Funding_comb_user = pd.concat([Funding_comb, User_fees])
Funding_comb_nouser = Funding_comb
Funding_comb_user["Financier"] = Funding_comb_user["Financier"].replace(
    dict.fromkeys(
        [
            "UU",
            "Chalmers",
            "KAW",
            "LiU",
            "SLU",
            "LU",
            "UmU",
            "Elixir",
            "Nordforsk",
            "Other",
            "Universities",
            "VR",
            "KTH",
            "SSF",
            "SU",
            "GU",
            "KI",
            "University hospital",
            "ALF",
            "Vinnova",
            "County council",
            "ÖRU",
        ],
        "Other funding",
    ),
    regex=True,
)

Funding_comb_nouser["Financier"] = Funding_comb_nouser["Financier"].replace(
    dict.fromkeys(
        [
            "UU",
            "Chalmers",
            "KAW",
            "LiU",
            "SLU",
            "LU",
            "UmU",
            "Elixir",
            "Nordforsk",
            "Other",
            "Universities",
            "VR",
            "KTH",
            "SSF",
            "SU",
            "GU",
            "KI",
            "University hospital",
            "ALF",
            "Vinnova",
            "County council",
            "ÖRU",
        ],
        "Other funding",
    ),
    regex=True,
)
# Below to check
# print(Funding_comb_nouser["Financier"].unique())
# print(Funding_comb_user["Financier"].unique())
tot_fund_nouser = (
    Funding_comb_nouser.groupby(["Facility", "Platform"]).sum().reset_index()
)
tot_fund_user = Funding_comb_user.groupby(["Facility", "Platform"]).sum().reset_index()

tot_fund_nouser.insert(
    loc=3, column="Total SEK", value=(tot_fund_nouser["Amount (kSEK)"] * 1000)
)
tot_fund_user.insert(
    loc=3, column="Total SEK", value=(tot_fund_user["Amount (kSEK)"] * 1000)
)

# print(tot_fund_nouser.head())
# print(tot_fund_user.head())

# The above will give you the totals that can be used for the x-axis
# need to figure out portions for the pie charts (portion of userfees vs sll funding vs other funding)
# original values in ksek, so *1000 converts to just SEK
# fill value is to fill in where there is 0 'other funding'
fin_fund_nouser = (
    Funding_comb_nouser.groupby(["Facility", "Platform", "Financier"])
    .sum()
    .unstack(fill_value=0)
    .stack()
    .reset_index()
)
fin_fund_nouser["Other fund SEK"] = fin_fund_nouser["Amount (kSEK)"] * 1000

fin_fund_user = (
    Funding_comb_user.groupby(["Facility", "Platform", "Financier"])
    .sum()
    .unstack(fill_value=0)
    .stack()
    .reset_index()
)
fin_fund_user["Other fund SEK"] = fin_fund_user["Amount (kSEK)"] * 1000

# add column for totals to fin_fund_nouser and fin_fund_user
# after this, work out proportions that will be used in pie charts
# subset to get values

fin_fund_nouser_sub = fin_fund_nouser[["Facility", "Financier", "Other fund SEK"]]
fin_fund_user_sub = fin_fund_user[["Facility", "Financier", "Other fund SEK"]]
tot_fund_nouser_sub = tot_fund_nouser[["Facility", "Total SEK"]]
tot_fund_user_sub = tot_fund_user[["Facility", "Total SEK"]]

props_user = pd.merge(
    fin_fund_user_sub,
    tot_fund_user_sub,
    how="left",
    left_on="Facility",
    right_on="Facility",
)

props_nouser = pd.merge(
    fin_fund_nouser_sub,
    tot_fund_nouser_sub,
    how="left",
    left_on="Facility",
    right_on="Facility",
)

props_user["Prop_funding"] = props_user["Other fund SEK"] / props_user["Total SEK"]
props_nouser["Prop_funding"] = (
    props_nouser["Other fund SEK"] / props_nouser["Total SEK"]
)

# The above now contains all the proportions required for each pie chart
# Later will have a function to extract everything

# Need to get y-axis values - just FTEs logged - and x axis values total funding (with/without users) into one dataframe (for simplicity)
FTE_data = Facility_data[["Facility", "FTEs"]]
# Total SEK is the values in SEK
nouser_fund = tot_fund_nouser[["Facility", "Total SEK"]]
user_fund = tot_fund_user[["Facility", "Total SEK"]]
# need to log total values and FTEs
FTE_data["log_FTE"] = np.log10(FTE_data["FTEs"])
nouser_fund["log_Total_SEK"] = np.log10(nouser_fund["Total SEK"])
user_fund["log_Total_SEK"] = np.log10(user_fund["Total SEK"])
# make separate df for the user and nouser total

axes_nouser = pd.merge(
    FTE_data,
    nouser_fund,
    how="left",
    left_on="Facility",
    right_on="Facility",
)

axes_user = pd.merge(
    FTE_data,
    user_fund,
    how="left",
    left_on="Facility",
    right_on="Facility",
)

# Draw plot with user fees NOT included
fig, ax = plt.subplots(figsize=(30, 30))
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)
plt.grid(axis="y", color="lightgrey", linestyle="-", linewidth=0.5)
for i in props_nouser["Facility"].unique():
    check = props_nouser[props_nouser["Facility"] == i]
    other = axes_nouser[axes_nouser["Facility"] == i]
    check = check[["Financier", "Prop_funding"]]
    check = dict(check.values)
    drawPieMarker(
        xs=float(other.log_Total_SEK),
        ys=float(other.log_FTE),
        ratios=list(check.values()),
        sizes=[1000],
        colors=[SCILIFE_COLOURS[8], SCILIFE_COLOURS[0], SCILIFE_COLOURS[12]],
    )
# set these limits to be appropriate for IAB 2021 results. might need change for other years.
plt.ylim(-0.1, 2.25)
plt.xlim(5.0, 8.0)
# \n just gives a line of space
plt.xlabel("\nTotal funding (log10)", fontsize=30)
plt.ylabel("FTE (log10) \n", fontsize=30)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
Other_fund = mpatches.Patch(color=SCILIFE_COLOURS[8], label="Other funding")
SciLifeLab_fund = mpatches.Patch(color=SCILIFE_COLOURS[0], label="SciLifeLab funding")
plt.legend(
    handles=[Other_fund, SciLifeLab_fund],
    bbox_to_anchor=(1.05, 1.05),
    ncol=2,
    handlelength=0.7,
    frameon=False,
    fontsize=30,
)
# plt.show()
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
plt.savefig("Plots/FundvsFTEs_nouserfees_v2.png", dpi=300)

# Draw plot with user fees included
fig, ax = plt.subplots(figsize=(30, 30))
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)
plt.grid(axis="y", color="lightgrey", linestyle="-", linewidth=0.5)
for i in props_user["Facility"].unique():
    check = props_user[props_user["Facility"] == i]
    other = axes_user[axes_user["Facility"] == i]
    check = check[["Financier", "Prop_funding"]]
    check = dict(check.values)
    drawPieMarker(
        xs=float(other.log_Total_SEK),
        ys=float(other.log_FTE),
        ratios=list(check.values()),
        sizes=[1000],
        colors=[SCILIFE_COLOURS[8], SCILIFE_COLOURS[0], SCILIFE_COLOURS[12]],
    )
# set these limits to be appropriate for IAB 2021 results. might need change for other years.
plt.ylim(-0.1, 2.25)
plt.xlim(5.0, 8.0)
# \n just gives a line of space
plt.xlabel("\nTotal funding (log10)", fontsize=30)
plt.ylabel("FTE (log10) \n", fontsize=30)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
Other_fund = mpatches.Patch(color=SCILIFE_COLOURS[8], label="Other funding")
SciLifeLab_fund = mpatches.Patch(color=SCILIFE_COLOURS[0], label="SciLifeLab funding")
U_fees = mpatches.Patch(color=SCILIFE_COLOURS[12], label="User fees")
plt.legend(
    handles=[Other_fund, SciLifeLab_fund, U_fees],
    bbox_to_anchor=(1.05, 1.05),
    ncol=3,
    handlelength=0.7,
    frameon=False,
    fontsize=30,
)
# plt.show()
if not os.path.isdir("Plots"):
    os.mkdir("Plots")
plt.savefig("Plots/FundvsFTEs_userfees_v2.png", dpi=300)
