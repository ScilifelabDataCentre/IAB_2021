"""This script generates all the wordclouds involving keywords assigned by authors for IAB 2021 report"""
# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import numpy as np
import os
from keyword_data_prep import (
    year1,
    year2,
    Fellows_data_range,
    Fellows_data_year1,
    Fellows_data_year2,
    key_words_fell_range,
    key_words_fell_year1,
    key_words_fell_year2,
    Facilities_data_range,
    Facilities_data_year1,
    Facilities_data_year2,
    key_words_fac_range,
    key_words_fac_year1,
    key_words_fac_year2,
    Affiliates_data_range,
    Affiliates_data_year1,
    Affiliates_data_year2,
    key_words_aff_range,
    key_words_aff_year1,
    key_words_aff_year2,
)


# IAB 2021 - interested in 2 years '19 and '20 - need to look over total range each year individually
# set years of interest in dataprep files!


# add whatever words you'd like to exclude
stopwords_fell = list(STOPWORDS) + [
    "None",
    "s",
]
stopwords_fac = list(STOPWORDS) + [
    "None",
    "s",
]
stopwords_aff = list(STOPWORDS) + [
    "None",
    "s",
]


# to make a square shaped wordcloud
mask = np.array(Image.open("SciLifeLab_symbol_POS.png"))

# SciLifeLab Visual Identity 2020
font_path = "Lato-Bold.ttf"
SLL_lime_colour = [76, 55, 53]
SLL_teal_color = [185, 92, 20]
SLL_aqua_colour = [186, 35, 46]
SLL_grape_color = [288, 46, 22]

# give colours
def multi_color_func(
    word=None,
    font_size=None,
    position=None,
    orientation=None,
    font_path=None,
    random_state=None,
):
    colors = [SLL_lime_colour, SLL_teal_color, SLL_aqua_colour, SLL_grape_color]
    rand = random_state.randint(0, len(colors) - 1)
    return "hsl({}, {}%, {}%)".format(colors[rand][0], colors[rand][1], colors[rand][2])


def makeauthkeywordcloud(data, Thresh_num, group_name, stopwords):
    wordcloud = WordCloud(
        background_color="white",
        stopwords=stopwords,
        font_path=font_path,
        mask=mask,
        min_font_size=14,
        width=mask.shape[1],
        height=mask.shape[0],
        collocation_threshold=Thresh_num,
        color_func=multi_color_func,
        prefer_horizontal=1,
        # This now includes hyphens in punctuation
        regexp=r"\w(?:[-\w])*\w?",
        # max word default is 200, can make more or less be in cloud
        max_words=200,
    ).generate(data)

    # plot the WordCloud image
    # line below might how red under figsize, but no issue.
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    if not os.path.isdir("Plots/Auth_keyword_clouds"):
        os.mkdir("Plots/Auth_keyword_clouds")
    # savefig will save the figure (at resolution 300dpi - good enoough for print)
    plt.savefig(
        "Plots/Auth_keyword_clouds/{}_authkeywordwordcloud.png".format(group_name),
        dpi=300,
    )


# note - 50 as a threshold for collocation is typically sufficient to stop weird word combinations in bigrams, but increase if strange 2 word phrases appear
# makeauthkeywordcloud(
#     key_words_fell_range, 10, "fell_authkeywords_2years", stopwords_fell
# )
# makeauthkeywordcloud(
#     key_words_fell_year1, 10, "fell_authkeywords_{}".format(year1), stopwords_fell
# )
# makeauthkeywordcloud(
#     key_words_fell_year2, 10, "fell_authkeywords_{}".format(year2), stopwords_fell
# )
# makeauthkeywordcloud(key_words_fac_range, 10, "fac_authkeywords_2years", stopwords_fac)
# makeauthkeywordcloud(
#     key_words_fac_year1, 10, "fac_authkeywords_{}".format(year1), stopwords_fac
# )
# makeauthkeywordcloud(
#     key_words_fac_year2, 10, "fac_authkeywords_{}".format(year2), stopwords_fac
# )
makeauthkeywordcloud(key_words_aff_range, 10, "aff_authkeywords_2years", stopwords_aff)
makeauthkeywordcloud(
    key_words_aff_year1, 10, "aff_authkeywords_{}".format(year1), stopwords_aff
)
makeauthkeywordcloud(
    key_words_aff_year2, 10, "aff_authkeywords_{}".format(year2), stopwords_aff
)
