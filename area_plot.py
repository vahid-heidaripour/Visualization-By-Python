import numpy as np
import pandas as pd

df_can = pd.read_excel('Canada.xlsx',
                        sheet_name='Canada by Citizenship',
                        skiprows=range(20),
                        skipfooter=2)

print('Data read into a dataframe!')

df_can.head()
df_can.tail()

print(df_can.shape)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

mapping = {df_can.columns[0]:'Country', df_can.columns[1]:'Continent', 
           df_can.columns[2]:'Region'}
df_can.rename(columns=mapping, inplace=True)

# let's examine the types of the column labels
# check to see if all elements in a list are string
all(isinstance(column, str) for column in df_can.columns)

df_can.columns = list(map(str, df_can.columns))

# let's check the column labels types now
all(isinstance(column, str) for column in df_can.columns)

df_can.set_index('Country', inplace=True)

df_can['Total'] = df_can.sum(axis=1)

print('data dimensions:', df_can.shape)

# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

# Area Plots
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df_can.head()

df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)

#df_top5.plot(kind='area',
             #stacked=False,
             #alpha=0.75, # 0-1, default value a=0.5
             #figsize=(20, 10))

#plt.title('Immigration Trend of Top 5 Countries')
#plt.ylabel('Number of Immigrants')
#plt.xlabel('Years')

#plt.show()




#print(df_can['2013'])
#count, bin_edges = np.histogram(df_can['2013'])
#print(count)
#print(bin_edges)
#
#df_can['2013'].plot(kind='hist', figsize=(20, 10), xticks=bin_edges)
#plt.title('Histogram of Immigration from 195 Countries in 2013')
#plt.ylabel('Number of Countries')
#plt.xlabel('Number of Immigrants')
#
#plt.show()


# Bar Charts
df_iran = df_can.loc['Iran (Islamic Republic of)', years]
print(df_iran.head())

df_iran.plot(kind='bar', figsize=(10, 6), rot=90) # 'barh' for horizontal 
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.title('Iranian immigrants to Canada from 1980 to 2013')

# Annotate arrow
plt.annotate('',                      # s: str. Will leave it blank for no text
             xy=(32, 11214),             # place head of the arrow 
             xytext=(28, 7493),         # place base of the arrow 
             xycoords='data',         # will use the coordinate system of the object being annotated 
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )

# Annotate text
plt.annotate('2008 - 2013 Financial Crisis', # text to display
             xy=(27.5, 7593),                    # start the text
             rotation=58,                    # based on trial and error to match the arrow
             va='bottom',                    # want the text to be vertically 'bottom' aligned
             ha='left',                      # want the text to be horizontally 'left' algned.
            )

plt.show()