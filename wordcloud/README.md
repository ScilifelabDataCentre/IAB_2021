## How to use wordcloud scripts

- Non python files: 
    - Lato-Bold.tff is the font used for wordclouds. To use a different font, replace this and specify the alternative font in the scripts responsible for producing the wordclouds themselves.
    - SciLifeLab_symbol_POS.png is the image used to shape the wordclouds. This is really just used to give a square. To use a different shape, just put in a new .png file with the desired shape and specify the alternative shape in the scripts responsible for producing the wordclouds themselves. 

- livewordcloud.py: this script was a draft on which the other scripts are based (used for the COVID portal), it was not used directly in the IAB report. 

- python scripts with 'data_prep' in the name: (i.e. WOS_key_data_prep.py, abstract_data_prep.py, keyword_prep.py, titles_data_prep.py). These scripts will prepare data sorted for the years of interest (you should specify these in the code). Just specify the years of interest and the source of data. The title of the script indicates what type of text data is dealt with by that script. In particular, WOS_key deals with keywords assigned by web of science, abstract deals with the abstracts of publications, keywords deals with author assigned keywords, and titles deals with the titles of papers. In 2021 IAB report, we used titles are they were most informative. 

- python scripts with 'wordcloud' in the name: (same format as data_prep, see above) these make wordcloud images for the last two years (here 19 and 20), the first year (here 2019), and the second year (here, 2020). Modifications should be made to change the stopwords as needed so that any uninformative words (e.g. 'the' are removed). Change the collocation threshold to exclude any weird word combinations in bigrams that don't make sense in isolation (e.g. sense in). Notes are in the script for additional guidance.