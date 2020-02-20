import numpy as np
import pandas as pd

df_can = pd.read_excel('Canada.xlsx',
                        sheet_name='Canada by Citizenship',
                        skiprows=range(20),
                        skipfooter=2)

print('Data read into a pandas dataframe!')

print('########### HEAD ###########')
print(df_can.head())

print('########### TAIL ###########')
print(df_can.tail())

print('########### INFO ###########')
print(df_can.info())

print('########### COLUMNS VALUES ###########')
print(df_can.columns.values)

print('########### INDEX VALUES ###########')
print(df_can.index.values)

print('########### SHAPE ###########')
print(df_can.shape)

print('########### REMOVE UNNECESSARY COLUMNS ###########')
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(df_can.head(2))

print('########### RENAME ###########')
mapping = {df_can.columns[0]:'Country', df_can.columns[1]:'Continent', 
           df_can.columns[2]:'Region'}
df_can.rename(columns=mapping, inplace=True)
print(df_can.columns)

print('########### ADD TOTAL ###########')
df_can['Total'] = df_can.sum(axis=1)
print(df_can['Total'])

print('########### NULLs ###########')
print(df_can.isnull().sum())

print('########### DESCRIBE ###########')
print(df_can.describe())

print('########### FILTERING COUNTRIES ###########')
print(df_can.Country)

print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]])

print('########### SET COUNTRY COLUMNS AS INDEX ###########')
df_can.set_index('Country', inplace=True)
print(df_can.head(3))

print('########### FULL ROW DATA ###########')
print(df_can.loc['Iran (Islamic Republic of)'])
# or df_can.iloc[row_numer]
# or df_can[df_can.index == 'Iran (Islamic Republic of)'].T.squeeze()

print(df_can[df_can.index == 'Iran (Islamic Republic of)'])

print('########### FOR SPECIFIC YEAR ###########')
print(df_can.loc['Iran (Islamic Republic of)', 2013])

print('########### FOR YEARs 1980 tp 1985 ###########')
print(df_can.loc['Iran (Islamic Republic of)', [1980, 1981, 1982, 1983, 1984, 1985]])

df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))

print('########### FILTERING BASED ON CRITERIA ###########')
condition = df_can['Continent'] == 'Asia'
print(condition)

print('########### PASS CONDITION INTO DATAFRAME ###########')
print(df_can[condition])

print('########### MULTIPLE CRITERIA ###########')
print(df_can[(df_can['Continent'] == 'Asia') & (df_can['Region'] == 'Southern Asia')])

print('########### MATPLOT ###########')
import matplotlib as mpl
import matplotlib.pyplot as plt

print('Matplotlib version: ', mpl.__version__)

print(plt.style.available)
mpl.style.use(['ggplot'])

iran = df_can.loc['Iran (Islamic Republic of)', years]
print(iran.head())

#iran.index = iran.index.map(int)
#iran.plot(kind='line')
#plt.title('Immigration from Iran')
#plt.ylabel('Number of immigrants')
#plt.xlabel('Years')
#plt.text(2010, 7418, '*')

#plt.show()

print('########### COMPARE ###########')
df_IS = df_can.loc[['Iran (Islamic Republic of)', 'Switzerland'], years]
df_IS = df_IS.transpose()
df_IS.index = df_IS.index.map(int)
df_IS.plot(kind='line')
plt.title('Immigrants from Iran and Switzerland')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show()