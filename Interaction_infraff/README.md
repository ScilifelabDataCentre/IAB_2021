## Notes for using scripts contained in this file

The files contained here generated plots (besides the venn diagram - see the 'venn' folder in the wider IAB repository).

- colour_science_2020.py: This file contains the colour codes for use in the plots. The colours will be automatically imported into the graphs.

- stacked_plot_interactions.py: This file creates a stacked bar plot showing the interactions between infrastructure and affiliated researchers (i.e. how many papers are just infra users, how many are from affiliated users, and how many involve both). To generate the data for this, it's easy to use the method outlined for the venn plots- see the notes in that repository.

- Interaction_table_and_bar.py: This script produces two things; (1) the table showing the main categories in which infrastructure users and affiliated researchers collaborate, and (2) the barplot showing the breakdown of collaborative projects labelled as either collaborative, technology development, or service (there is also a function to produce this as a table, but we didnt use this). The latter requires a little bit of manual work to get unique values for the labels (some publications can have more than one label, we used unique labels so if e.g. the labels given were 'service, service, service' we considered it a 'service' paper, if the labels were 'collaborative, service' the publication was considered both a service and a collaborative paper).