import pandas as pd


#df = pd.read_csv('pokemon.csv')

df = pd.read_csv('https://raw.githubusercontent.com/golsah/Python/main/pokemon_data.csv')

# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

#df = pd.read_csv('pokemon_data.txt', delimiter='\t')

#Printing the header with 5 first rows (default)
#print(df.head())

#Printing the 5th bottom rows (default)
#print (df.tail())

#print(df.head(10))

#df['HP']

## Read Headers
#print(df.columns)

## Read each Column
#print(df[['Name']])

## Read multiple colums

#print(df[['Name', 'Type 1', 'HP']])

## Read Each Row (index location)
#print(df.iloc[1])

## Read Multiple Rows (index location)
#print(df.iloc[0:])

## Read a specific location (R,C)
#print(df.iloc[2,1])

## To access only the rows with a specific value of a column (with loc)
#print(df.loc[df['Type 1'] == "Grass"])

# Describes the values of tables
#print(df.describe())

# Sorting values by Name
#print(df.sort_values('Name', ascending=True))

# Sorting according to two features
# 1: ascending 0:descending validation to Sorting Values ['Type 1', 'HP'], ascending=[1,0]
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


# Creating a new column "Total" that is the sum of some other columns. 
# In this way, e.g., we can find out which Pokemon is the best
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#df.head(5)

# Another way to create the proposed "Total" column. Using 'sum(axis=1)' specifies that adding is horizontally
#df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# Removing a column
#df = df.drop(columns=['Total'])

# Reordering columns: The last column(-1) is now the 5th column
#cols = list(df.columns) 
# Getting columns as a list to prepare for doing the reordering
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

#print(df.head(5))

#df.to_csv('modified.csv', index=False)

#df.to_excel('modified.xlsx', index=False)

#df.to_csv('modified.txt', index=False, sep='\t')



#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#print(new_df)

#new_df2 = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]
#new_df2

# To get new indeces
#new_df = new_df.reset_index (drop=True)
#print(new_df)

# If you do not want to reset it into a new data frame and conserves a little bit of memory, just do it in place
#new_df.reset_index (drop=True, inplace=True)
#print(new_df)

#Filtering based on an info inside the column
#print(df.loc[df['Name'].str.contains('Mega')])

# Not included with the squiggly line (~)
#print(df.loc[~df['Name'].str.contains('Mega')])

# To have more complex filtering with 'regex'
# first, import regular expressions: so powerful filtring based on certain textual patterns
import re 
#print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])

# No case sensitive filtering with 'flags=re.I'
#df1 = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
#print(df1)

# Filtering based on some part of the column value, e.g., pikachu --> pi
#df1 = df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)]
# '*' meant zero or more
#print(df1)

#specify the start of the line by the 'carrot' symbol
#df1 = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
#print(df1)

# To save the new data
#new_df.to_csv('filtered.csv')


#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
#print(df)

#df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
#print(df)

# modify a column based on the info from another column
#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
#print(df)


# retrieve the original modified data
#df = pd.read_csv('modified.csv')

# Changing multiple parameters at the same time (e.g., Generation and Legendary). In this case, you should pass them in a list
#df.loc[df['Total'] > 500, ['Generation','Legendary']] = "TEST VALUE"

# or modify them individually
#df.loc[df['Total'] > 500, ['Generation','Legendary']] = ['Test 1', 'Test 2']
# In this example, we specified what generation becomes and what legendary becomes if the condition "Total>500" is met.

#print(df)


# Let's start by loading in that check pointed CSV we created 
#df = pd.read_csv('modified.csv')

# To see the average HP and attack of all the Pokemon grouped by which type they are.
# we will get all the stats broken down by their mean sorted by what type one is.
#print(df.groupby(['Type 1']).mean())

# Making this more useful by using the 'sort' function
#print(df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

#print(df.groupby(['Type 1']).sum())

# To get the total number of each Pokemon
#print(df.groupby(['Type 1']).count())

# to just get the count column 
#df['count'] = 1 # Filling one in a column added to the data frame
#print(df.groupby(['Type 1']).count()['count'])


# Grouping by multiple parameters at the same time
#df['count'] = 1
#print(df.groupby(['Type 1', 'Type 2']).count()['count'])


# passing in n rows at a time
# This loaded in the data frame but in chunks of five
for df in pd.read_csv('modified.csv', chunksize=5):
# It means that our df would be 5 rows of the main dataset (i.e., modified.csv)
    print("CHUNK DF")
    print(df)