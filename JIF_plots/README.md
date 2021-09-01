## How to use JIF scripts

(maybe we should consider using Eigen factor (article influence for the normalised score) in place of JIF for future years) 

- Colour_science_2020.py: this includes all the colours you will need to use to create the plots with the correct visual identity for 2021. Update as needed to match visual identity in future years.

- Python scripts with data_prep in the title: Uses data from the publications database (USE THE RAW EXTRACTS FOR THESE PLOTS) together with data extracted from the Clarivate database on JIF score to match JIF scores to papers. The scripts categorise the JIF scores to the ones used in this and previous reports. Whilst the plot scripts pulls data from here directly the script should be used to print out a file of matches - called 'Check_me_manual_improve.xlsx'. Not everything will match correctly without manual intervention, check that excel file to see how improvements might be improved. Rerun the script with corrected files to ensure corrections have worked. When satisfied that the level of matching has been maximised, the plot script can be used. 

- JIF_plot.py: pulls data from the data preperation scripts for each group (currently fellows, infastructure users and affiliated researchers) to produce the plots. In IAB 2021, the timeframe used to assess infrastructure users and affiliates was 2013-20, consistent with a change in mandate. For fellows it was 2014-20, to align with the start of the program. Changes should be made to reflect the appropriate years.