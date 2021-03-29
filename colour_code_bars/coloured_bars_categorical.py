"""This script can be used to construct bar charts coloured
according to an impact factor (e.g. MNCS/PP(top10)
the colours will be categorical'"""
import plotly.express as px
import pandas as pd
#read in data
df = pd.read_excel('/Users/liahu895/Documents/testdata/test_bars.xlsx',
    sheet_name='Sheet 1',
    engine='openpyxl')
#calculated mean and count
summarised = df.groupby('Field').agg(Count=('Field', 'size'),
    mean_value=('Value', 'mean')).reset_index()
#bin data to categorise colouring
bins=[-1.0, 0, 3.33, 6.66, 9.99, 100.0]
labels=['Otillräckligt underlag', '0.00-3.33', '3.33-6.66', '6.66-9.99',
        '>9.99']
summarised['binned']=pd.cut(summarised['mean_value'], bins=bins, labels=labels)
summarised.sort_values('binned', ascending=False, inplace=True)
#produce figure
fig=px.bar(summarised, x='Field', y='Count',
    color='binned',
    color_discrete_map={'Otillräckligt underlag':'black',
                        '0.00-3.33':'rgb(73, 31, 83)',
                        '3.33-6.66':'rgb(4, 92, 100)',
                        '6.66-9.99':'rgb(167, 201, 71)',
                        '>9.99':'rgb(76, 151, 159)'})
fig.update_xaxes(title='', showgrid=True, linecolor='black',
    tickprefix='<b>', ticksuffix='</b>')
fig.update_yaxes(title='<b>Number of Publications</b>',
    showgrid=True, gridcolor='black',
    linecolor='black', tickprefix='<b>', ticksuffix='</b>', range=[0,62])
fig.update_layout(plot_bgcolor='white', legend_title_text='<b>Mean value</b>',
    coloraxis_colorbar=dict(
    tickvals=[1, 2, 3],
    ticktext=labels, titleside='top'
))
#to 'show' the figure in browser
#fig.show()
#to write the file as .png
fig.write_image('cat_col_bar.png', scale=2)
#write out as html for web
#fig.write_html('cat_col_bar.html', include_plotlyjs=False, full_html=False)
