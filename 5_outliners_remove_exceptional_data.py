# Outliers: It's a process of removing exceptional data using statistics.
# Example of outliers in python using pandas and numpy?
# Outliers use to remove the data with is outer side of the average dataset reange. I'm taking an exaple of exam number in which might a exam of 100 number and most of students scroed between 40 to 60 but one studnet got 5 and one studnet got 99 as per this those other 2 studnets fot outside of range data so as per this those 2 students data are exceptional case and as per mantaing the ratio we need to remove those 2 data but what if we have very huge amount of data not limited data. So on that casae we need to use the concept of Outliers. So as per this we need a set of formulas to solve this problems.

# Like in this casae we have to know
# Mean: Sum of all numbers and divid the number with count of total numbers. Like: 1+2+3+4+5/5 as per this we get mean value
# Medion: Its a middle number of the total number. Like 1,2,3,4,5 as per this the median number is 3
# Mode: Its the numebr which occure maximum type. Like 1,2,3,4,4,5 as per this the 4 is Mode number
# Range: It's find by largest_number - smallest_number = range

# After understaning of the concept of mean, medion, mode and range know time to understand how to find the Outliners and how to remove them. So for that I am going to explain this on points:
# 1. Standard Deviation: For finding the standard deviation follow the process. Lets take an example of students exam makrs. which we discussed earlier.
#     a. Mean Value: First need to found means value so as per the we get the difference between hight and lower values.
#         So most of the number are between 40 to 60 so as per that lets asume the total student exam numbers are:

# For finding the Outliers we need to have 3 values: mean value, variance value and standard deviation 

import math

# first of all we need to have data like i take a example data here of stunds
exam_numebrs = [3,40,45,55,53,59,60,99]
# find the average value of the exam number which is normally the mean value
average_of_exam_numbers = sum(exam_numebrs) / len(exam_numebrs)
print('\naverage_of_exam_numbers:\n\n', average_of_exam_numbers)
# find difference between the values form this average values:
difference_values = []
for num in exam_numebrs:
    difference_values.append(num - average_of_exam_numbers)    
print('\ndifference_values:\n\n', difference_values)
# varianece_value: for finding the need to square each difference value individually and sum all value to get the varience 
variance_value = []
for num in difference_values:
    variance_value.append(num ** 2)
variance = sum(variance_value)
print('\nVariance:\n\n', variance)
# standard deviation value is just do square root to variance value
standard_deviation = math.sqrt(variance)
print('\nstandard_deviation\n\n', standard_deviation)

# Know we know how to find the standard deviation value so lets find the Outliers 
# for finding the Outliers I am going to use the walmart sales data to find the Outliers:
import pandas as pd
import numpy as np

df = pd.read_csv('resources/walmart.csv')
print('\nWalmart Data:\n',df)
# Understand that what requred for finding the Outliers: Here I am taking a example of walmarts weekly sales
# 1. Requere to have min value and max value of walmart weekly sales.
# 2. Find the q1 and q3, for that use the numpys percentile method in which pass 2 arguments first the walmarst weekly sales columna and 2nd is pass list [25,75] which is q1 and q3
# 3. THen find IQR: Interquartile Range by this formula: q3 - q1 thats how find the Interquartile Range
# 4. Then check lower extrem: q1 - 1.5 * IQR and for upper extrem: q3 + 1.5 * IQR
# 5. Cheak lower and upper outliner in walmart via weekly sales colum. 

# 1. Let's find the min and max values
min_sales_value = df['Weekly_Sales'].min()
max_sales_value = df['Weekly_Sales'].max()
print('\nMin and Max values:\n', min_sales_value, ' ', max_sales_value)
# 2. find q1 and q2
q1, q3 = np.percentile(df['Weekly_Sales'], [25,75])
print('\nQuartile values of q1 and q2:\n', q1,' ',q3)
# 3. find iqr: Interquartile range
iqr = q3 - q1
print('\niqr: \n', iqr)
# 4. find lower_extrem and upper_extrem by following formula
lower_extrem = q1 - 1.5 * iqr
print('\nlower_extrem:\n', lower_extrem)
upper_extrem = q3 + 1.5 * iqr
print('\nupper_extrem:\n', upper_extrem)
# 5. find outlier by checking weekly salres value min and max value with lower and upper extrems
is_lower_outlier = lower_extrem > min_sales_value
print('\nis_lower_outlier:\n', is_lower_outlier)
is_upper_outlier = upper_extrem < max_sales_value
print('\nis_upper_outlier:\n', is_upper_outlier)
# 6. Got upper outlier know need to got no outlier data so for that apply the formula to get only no outlier data 
no_outlier_data = df.loc[(df['Weekly_Sales'] < upper_extrem ) & (df['Weekly_Sales']>lower_extrem)]
print('\nno_outlier_data: \n', no_outlier_data)
