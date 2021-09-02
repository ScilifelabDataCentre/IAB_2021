## Notes on the scripts included in this folder

A considerable amount of analysis was completed to examine the relative performance of SciLifeLab, both in different fields and over time. As such, there are multiple scripts to do different things.

- trends_aff.py and trends_fac.py: these scripts generate line plots to show how work in different fields changes over time for affiliates and infrastructure users, respectively. The y axis shows the proportion of papers published in those categories (the top 6 areas in which SciLifeLab publishes). The x-axis shows years (2015-18). The points are sized relative to PP(top10) score. the points are coloured with respect to whether the PP(top10) score exceeds the relevant benchmark value for Sweden.

- Topcategories_affstable.py, Topcategories_facstable.py, and Topcategories_fellstable.py: These scripts create tables showing the 'top' categories in which each of affiliates, infrastructure users and fellows publish (i.e. where they publish most). Used 2015-2018 as a timeframe. 

- no_pubs_compared_Sweden.py: This script calculates the number of publications in each of the 'top 6' categories for affiliates and infrastructure users compared to the number produced by Sweden in general.

- Matrix_bubble_units_top6fields.py: This creates a matrix bubble plot showing the relative number of publications produced by each unit in different fields.

- facilities_and_fields_top3table.py: This creates a table that shows the 3 categories in which each infrastructure unit publishes.

- colour_science_2020.py: This allows coordination to the visual identity.

- benchmarking_pptop10_15to18.py: This creates the plots shown to compare the PP(top10) scores of infrastructure users and affiliates compared to those for Sweden. This is an update to benchmarking_PPtop10.py, which focussed on the latest year (2018).

- benchmarking_mncs_15to18.py: This creates the plots shown to compare the MNCS scores of infrastructure users and affiliates compared to those for Sweden. This is an update to benchmarking_MNCS.py, which focussed on the latest year (2018).