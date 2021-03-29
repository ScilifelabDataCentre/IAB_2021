"""This script can be used to construct bar charts coloured
according to an impact factor (e.g. MNCS/PP(top10)
colours will be continuous'"""
import plotly.express as px
import pandas as pd
#read in data
df = pd.read_excel('/Users/liahu895/Documents/testdata/test_bars.xlsx',
    sheet_name='Sheet 1',
    engine='openpyxl')
#calculated mean and count
summarised = df.groupby('Field').agg(Count=('Field', 'size'),
    mean_value=('Value', 'mean')).reset_index()
#produce figure
fig=px.bar(summarised, x='Field', y='Count',
    color='mean_value', color_continuous_scale=[[0, 'rgb(73, 31, 83)'],
    [0.5, 'rgb(4, 92, 100)'], [1, 'rgb(167, 201, 71)']])
fig.update_xaxes(title='', showgrid=True, linecolor='black',
    tickprefix='<b>', ticksuffix='</b>')
fig.update_yaxes(title='<b>Number of Publications</b>',
    showgrid=True, gridcolor='black',
    linecolor='black', tickprefix='<b>', ticksuffix='</b>', range=[0,62])
#continuous colourbar layout
fig.update_layout(plot_bgcolor='white', coloraxis_colorbar=dict(
    title='<b>Mean value</b>', titleside='top',
    tickprefix='<b>', ticksuffix='</b>'))
#to 'show' the figure in browser
#fig.show()
#to write the file as .png
#fig.write_image('cont_col_bar.png', scale=2)
#write out as html for web
fig.write_html('cont_col_bar.html', include_plotlyjs=False, full_html=False)
