import numpy as np
import pandas as pd

df_can = pd.read_excel('Canada.xlsx',
                        sheet_name='Canada by Citizenship',
                        skiprows=range(20),
                        skipfooter=2)

print('Data read into a pandas dataframe!')

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

mapping = {df_can.columns[0]:'Country', df_can.columns[1]:'Continent', 
           df_can.columns[2]:'Region'}
df_can.rename(columns=mapping, inplace=True)

df_can.columns = list(map(str, df_can.columns))

df_can.set_index('Country', inplace=True)

df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

# Pie plot
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

# group countries by continents and apply sum() function 
df_continents = df_can.groupby('Continent', axis=0).sum()

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 6),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,
                            pctdistance=1.12,
                            colors=colors_list,
                            explode=explode_list)

plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12)
plt.axis('equal') # Sets the pie chart to look like a circle.
plt.legend(labels=df_continents.index, loc='upper left')

plt.show()