import pandas  as pd

product = pd.read_csv('resources/Products.csv')
customer = pd.read_csv('resources/Customers.csv')

print('\nGet Products:\n')
print(product.head())

print('\nGet Customers:\n')
print(customer.head())

# merge(): inner join: get those products who have customer records.
print('\n\nInner Join: get those products who have customer records\n')
print(product.merge(customer, on='Product_ID').head())

# In case want to get the custoemr who have matching product name in product table
# but in this case in product table product name is stored as purchased_product and in customer table have product_name column in this casae use two parameters in the same merge() method 
print('\n\nGet the product who is exisis in product and customer table\n')
print(product.merge(customer, left_on='Product_name', right_on='Purchased_Product'))

# merge() method is also a very powerful because as see on line 19 where used left_on and right_on where gave the column name form both table by which fetch the data but these two also accepts series values means more then on left side columns and right side columns will define here and as per that will fetch the data.
# Like where product id and seller city similer on product and custome table fetch all that data 
print('\n\nFetch data where product id and seller city are similer in both tables:\n')
print(product.merge(customer, how='inner', left_on=['Product_ID','Seller_City'], right_on=['Product_ID','City']))


# Outer join or Full Join: same in merge() method pass how='outer'
# Same as database conscept dosen't matter left or right table data matching or not it fecth the data row wise like in this case left tale have data but right table have nothing so get NaN on right side of the record.
print('\n\nOuter join or Full Join: same in merge() method pass how=outer\n')
print(product.merge(customer, how='outer').head())
print('\n\nGet outer join data as per product id:\n')
print(product.merge(customer, on='Product_ID', how='outer')) # this will only fetch 6 records who have similer data but other are NaN


# Left join: merege(): similer jsut pass how='left' will provide all the left side data don;t matter right table data match or not
print('\n\nLeft join:\n')
print(product.merge(customer, how='left').head())
print('\n\nGet left join data as per product id:\n')
print(product.merge(customer, on='Product_ID', how='left'))


# right join: merge(): similer pass how='right' to get all the data form right table dosn't matter left have the data or not
print('\n\nRight join:\n')
print(product.merge(customer, how='right'))
print('\n\nRight join as per product id:\n')
print(product.merge(customer, on='Product_ID', how='right'))



# Concate two datafreame or csv file: In this case need to have both tables or csv have similer name of columns so that merge them ohterwise at first make both tables or csv files columns similer then perform the concat() 

# 1. get 2 csv file and store both on two varibales then as per the pd which is pandas by whcih load both csv like on store in 2 varibales like: df1 and df2 then write like this:

# pd.concat((df1, df2))   # this is just as simple as it looks