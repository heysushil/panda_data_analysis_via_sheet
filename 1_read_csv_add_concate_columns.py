import pandas as pd

df = pd.read_csv('resources/Pokemon.csv')

# Concate Type 1 and Speed as Type Power column which add as a new column in csv file
df['Type Power'] = df['Type 1'] + '-' + df['Speed'].astype(str) # Direct change datatype using astype method
print(df.head()) # head() method use to fetch specific rows form df, by defualt it provides 5 first rows.


# Add hp, attack, defense as a Power and only show name, hp, attack, defense and power columns
df['Power'] = df['HP'] + df['Attack'] + df['Defense']
power_df = df[['Name','HP','Attack','Defense','Power']]
print(power_df.head()) # head() method use to fetch specific rows form df, by defualt it provides 5 first rows.

# Remove default index and fetch data as per power
power_data = power_df.set_index('Power').sort_index()
print(power_data)


# Fetch only those pokes who have power more then 200
# power_data