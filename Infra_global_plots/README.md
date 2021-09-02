## Information regarding the scripts in this repository

##### Note that python 3 uses 'bankers rounding', so values are rounded to the nearest even value. However, values are requested to be rounding according to the '0.5 rounds up' rule

- Academicuser_pie.py: This script generates a pie chart related to the academic user distribution (Figure 10 in IEC report, Figure 20 in IAB report).

- colour_science_2020.py: this script includes all of the colours required to produce the infrastructutre plots in this repository. It may need updating in future years to correspond with updates to the visual identities of scilifelab etc.

- Funding_by_unit_barplot.py: Generates stacked barplot with units on x-axis, funding amount on y-axis, stacks divided by SciLifeLab, University funding and other funding (Figure 8 in 2020 IEC report).

- Funding_dist_infra.py: Generates a pie chart showing funding by platform (e.g. figure 7 in previous IEC report).

- Funding_nat_dist.py: Generates a pie chart showing funding related to individual national universities (e.g. figure 4b in previous IAB report).

- Funding_national_and_DDD.py: Generates a pie chart to show costs attributed to different sectors (e.g. figure 5 in IEC report)

- FundingPies_individual_platforms.py: This script generates individual plots for funding for individual platforms. Some manual manipulation will be needed to adjust labels so that they fit nicely - there is code for different styles within the script. It is recommended to make everything in one style and then make adjustments to the graphs that need it. The background for the graphs is transparent because this aids with layout.

- fundvspub_scatter.py: creates scatterplot of funding(log10) (x), publications(log10) (y), points coloured by platform. There are a few options for different versions - some exclude compute and storage, others don't. Notes are in the script to help.

- IEC_Uni_plot.py: script to make scatterplot of IEC university scores for units. There is a significant amount of script commented out. This script adds annotations to the points. These were not used in IAB 2021 because the graphs looked a little unclear. If they are added in future years, manual changes will be needed to the relative position of the text and the text label.

- input_data.py: This is included to enable infrastructure unit names to be mapped to their labels. You just need to input the correct data to use in future years. It feeds automatically into other scripts.

- piechart_scatter.py: This generates a scatterplot of pie charts related to funding. There are two versions, one shows user fees and one doesn't. It pulls in data from fundvspub_scatter.py. So, adjust that script first as needed, some changes to labels might be required.

- Proportions_type_pubs.py: This is a partial draft script based on qualifier labels. Not used for the report, might be useful in future.

- total_plat_funding_pie.py: This produces a pie chart showing total funding for all platforms combined. Some changes will be needed in each year to format the labels to minimise the space they occupy.

- Total_SLLaneext_funding.py: This script will generate a pie chart like figure 6 in IEC report, describing scilifelab and external funding.