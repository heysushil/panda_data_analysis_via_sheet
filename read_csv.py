import pandas as pd

# get csv file
data = pd.read_csv('resources/Pokemon.csv')

# head(): Get n number of rows form all data, by default it provide first 5 rows but define int number to get specific number of records.
get_all_data = data.head(2)

# set_index(): by default dataFrame provide index form 0 to number of rows but in case we want to define index name then use this to define.
# set_index(): is use to make any column as index or create any new. Its work to group realted data as per the inxex like below one example in which created manual dataFrame with 3 columns: name, age, city.
# In this set age as index and as per this: fetch the data as per age 
data_power = data.set_index('Power')

print(data_power.head())

# import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'Paris', 'London', 'Tokyo']
})

# Create a new index based on the 'age' column
df = df.set_index('age')

# Print the DataFrame
# print(df)


exit()

# Add new field Type Speed using Type 1 and Speed columns as showing result as Type 1 value - Speed
data['Type Speed'] = data['Type 1'] + '-' + data['Speed'].astype(str)

# print(data.columns)
# Create a new varibale as power which only show 5 columns: Name, HP, Attack and Defense in which have condion sum hp, attack, defence as Power
power = data[['Name','HP','Attack','Defense']]
power['Power'] = power['HP'] + power['Attack'] + power['Defense']
# print(power)

# Loop row 
# for index, row in data.iterrows(): # fetch all rows form csv
for (colname, colval) in data.iteritems(): # fetch all columns name in loop using iteritems() method
    # print(index, row['Name'])
    print(colname)