import pandas as pd

# get csv file
data = pd.read_csv('resources/Pokemon.csv')
print(data.head());exit()

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