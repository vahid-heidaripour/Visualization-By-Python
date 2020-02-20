import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

df_ci = df_can.loc[['China', 'India'], years].transpose()

print(df_ci.describe())

#df_ci.plot(kind='box', figsize=(8, 6)) # , vert=False makes it horizontal 
#
#plt.title('Box plot of Chinese and Indian Immigrants from 1980 - 2013')
#plt.ylabel('Number of Immigrants')
#
#plt.show()


# Subplots
fig = plt.figure() # create figure

ax0 = fig.add_subplot(1, 2, 1) # add subplot 1 (1 row, 2 columns, first plot)
ax1 = fig.add_subplot(1, 2, 2) # add subplot 2 (1 row, 2 columns, second plot)

df_ci.plot(kind='box', figsize=(15, 6), ax=ax0)
ax0.set_title('Box Plots of Immigrants from China and India (1980 - 2013)')
ax0.set_ylabel('Number of Immigrants')
ax0.set_xlabel('Countries')

df_ci.plot(kind='line', figsize=(15, 6), ax=ax1)
ax1.set_title ('Line Plots of Immigrants from China and India (1980 - 2013)')
ax1.set_ylabel('Number of Immigrants')
ax1.set_xlabel('Years')

plt.show()
