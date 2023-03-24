import pandas as pd

# get csv file and store in df which is know a DataFrame
df = pd.read_csv('resources/Pokemon.csv')
# print(df);exit()

# head(): Get n number of rows form all df, by default it provide first 5 rows but define int number to get specific number of records.
get_all_data = df.head(2)

# set_index(): by default dataFrame provide index form 0 to number of rows but in case we want to define index name then use this to define.
# In this set age as index and as per this: fetch the df as per age 
type_data = df.set_index('Type 1')

# This output is based on set Type 1 as index and in type 1 store a type of pokes which type of them so as per them 
print('\n\nSet Single Index: Type 1\n')
print(type_data.head())

# Set 2 index: Type 1 and Type 2 set as an index, when run get these two as an index 
two_index_data = df.set_index(['Type 1', 'Type 2'])
print('\n\nMulti Index Output\n')
print(two_index_data.head())

# set_index(): is use to make any column as index or create any new. Its work to group realted df as per the inxex like below one example in which created manual dataFrame with 3 columns: name, age, city.
manualDF = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'Paris', 'London', 'Tokyo']
})

# Create a new index based on the 'age' column
manualDF = manualDF.set_index('age')
print('\n\nSet index: age\n')
print(manualDF.head())

# reset_index: Reset index will include the defualt index number form 0 to available row records
print(manualDF.reset_index().head())
print('\n\nReset Index: age\n')
print(manualDF.reset_index(drop=True).head()) # Remove included age index by drop=True argument


# subsetting the df: Using to only fetch the values where found these on Type 1 column. This is using to filtter the data.
type1 = ['Rock','Fire']
subset_df = df[df['Type 1'].isin(type1)].sort_index()
print('\n\nSub-set data\n')
print(subset_df.head())

# loc: Same subsetting or filtter
# print(df.loc[type1])
print(df.loc[df['Type 1'].isin(type1)].sort_index().head())


# set_index(): multi index in same using [] bracket
multi_index = df.set_index(['Type 1','Type 2']).sort_index()
print('\n\nMulti Index Output\n')
print(multi_index)


# Multilevel indexing with subsetting: First defined columns in multi_level variable then define what specific data get form  the column is defined in rows_to_keep
# It helps to fillter the data as per columns specific values like here form Type 1 only filter Bug and form Type 2 filtterd Electric 
# multi_index_speed = df.set_index(['Speed','Generation'])
rows_to_keep = [('Bug','Electric'),('Grass','Poison'),('Rock','Fairy')]
print('\n\nMultilevel indexing with subsetting ')
print(multi_index.loc[rows_to_keep])


# slicing index value using loc(): this method only workes when you slice a unique column otherwise it will produce a key error. check unique using is_unique argument. Alternative fo this is iloc
# Also if single column have no unique value then make more then one columns combination to make uniqnes similer like database type of logic for fetching data.
# slicing data as per row/column wise using loc() method
multi_slice = df.set_index(['Type 1','Type 2'])
rows_to_keep = [('Bug','Electric'),('Grass','Poison')]

print('\n\nSlicing data: \n')
print(df.index.is_unique)
print(multi_slice.loc[rows_to_keep])


# slicing timesearice

# iloc(): slice by row number only or by row and column both. like a csv data in a matrix form which have row and columns combination.
print('\n\nSlicing using iloc():\n\n')
print(df.iloc[0:2]) # get a range data form 0 index to 2 it follows the n-1 rule to gave only 2 rows 0 and 1 only.
# print(df.iloc[0]) # this is provide only single row which is the columns and one row data only
print(df.iloc[1,1]) # it fetch sepcific index value similer like numarray

# Slicing also fetch data as per row and column wise. in which first is to get range of rows and second is for column
print(df.iloc[:,0:5].head()) # 0:5 use to fetch form 0 to 4th columns and first 5 records because used head() method. Its usefull to fetch only specific columns form csv.

# print(df)