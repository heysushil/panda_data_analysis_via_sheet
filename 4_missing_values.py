# Handle missing values and how to fill the missing values with dummy values lets learn and do exampels related to that

import pandas as pd

df = pd.read_csv('resources/miss.csv')

print('\n\nComplete data:\n\n',df,'\n\n')

# info(): provide all available columns with related datatypes.
# give total rows, total columns
print('\n\nCheck Info\n\n',df.info(),'\n\n')

# isnull(): give null values as true and non-null values as false. Its use when check the values in large amount. yet might be you thing what is this why i chek null and non-null values as true false but it workes on large scale daata whare manupulate the data and fill missing values as per this.
print('\n\nCheck Null values:\n', df.isnull(),'\n\n')

# isnull().sum(): provide total missing values count column wise to know how many null values are in each columns.
print('\n\nCheck is null sum: how many null values:\n\n', df.isnull().sum(),'\n\n')


# notnull(): provide all non-non values as truse and null values as false same like isnull() method
print('\n\nCheck not null value: using notnull() method\n', df.notnull(), '\n\b')

# notnull().sum(): same like count null values column wise also count the non-values columns wise
print('\n\nCount not-null valuse: notnull().sum()\n', df.notnull().sum(),'\n\n')


# Drop all with any missing values. there is two pareameters in dropna() method: any or all. Means if fond any null values will delete or if found all values then delete. It's like condition
print('\n\nDelete missing values: dropna()\n', df.dropna(), '\n\n')

# dropna(how='any'): delete record in which have any null value
print('\n\nDelete values where found any null: dropna(how="any"): \n\n', df.dropna(how='any'))

# dropna(how='all'): delete record where found all the records are null. if not fund any row which have all columns null then it will not delete the reocrd
print('\n\nDelete values where found all null values: dropna(how="all"):\n\n', df.dropna(how='all'))


# dropna(how='any', thresh=4): thresh means provide a condion like here provide a condition: if in dataFrame any row who have less then 4 non-null values then remove. Means if any row the less then 4 values and all other are null then will remove.
# thresh: when want to get all the rows where non-null values have specific number. Like a row have 5 columns and we want all the rows where have at least 3 non-null values then use thresh=3 to get all the rows which follow this senario.

# This line produce TypeError because in this 43 line number pass how and thresh both on dropna()
# print('\n\nDelete value as per thres: dropna(how="any", thresh=4)\n\n', df.dropna(how='any', thresh=4))


# thresh: filtter only those rows where at leash 5 columsn have non-null values using thresh=5
print('\n\nCheck if row have 4 or more Non-Null values: thresh: \n\n', df.dropna(thresh=5), '\n')

# subset: when want to only filtter non-null data as per specific columns basis then use subset. It's a 3rd parameter in dropna() method. Also we can use susbet with how and thresh. Because in this case we can at first filter with how where we want all or any NaN then subset for specifing in which columns basis we are going to filtter the data then at last if we want to specify that at least how many columsn we want non-null, for that use thresh.
# how and thresh both not allowed on same method because how filtter data as per if any or all data of row willl NaN and delet, same concept followed by thrash but in thresh we can speficy how many columns at least we want non-null means other columns will be null so that means both how and thrash do the same type of fillter but with there ways. Thast's why at same time both not allowed on dropna() method
print('\n\nFilter data as per specific columns basis using: subset: \n\n', df.dropna(subset=['city','state','age'], thresh=2),'\n')

# Other then NaN foun in rows like: - or space then what we do?
# use numpy to replace the unwanted char to NaN or what ever we want at the palce of these chars.
# pandas also have method to repalce any char with anyother.
import numpy as np

df = pd.read_csv('resources/miss2.csv')
print('\n\nNew Data Set in which have - or spaces:\n\n', df,'\n')

remove_special_char_df = df.replace('-',np.NaN).replace(' ',np.NaN)
print('\n\nReplace - or space using numpy: \n\n', remove_special_char_df)
# As per this only 10th record any no any NaN in reocrd thats why we get only 10th row
print('\n\nAfter replace - or spance to NaN use dropna to remove all NaN data:\n\n', remove_special_char_df.dropna(),'\n')

# Pandas also have fillna method to replace NaN value with any other as per our requirments
print('\n\nReplace - or space using df.fillna() method: \n\n', remove_special_char_df.fillna(0))
# But in case some columns values not acceptes or good to provid int value that what shoud do?
# fillna() method also allow to define the values inside this method to dict 
replace_values = df.fillna(
    {
        'id':0,
        'age':0,
        'fname':"no name",
        'lname':"no name",
        'city':"no city",
        'state':"no state"
    }
)
print('\n\nReplace non-int values using fillna() method:\n\n', replace_values,'\n')


