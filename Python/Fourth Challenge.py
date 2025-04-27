#Question 
#Find the Sum of a Column from Pandas Dataframe
#INPUT: [(101,1000),(201,2000),(301,3000),(401,4000),(501,5000)]
#OUTPUT: 15000

#Code Answer

# Python code​​​​​​‌‌​‌​​‌‌​‌‌​‌​​‌‌‌‌​‌​​‌‌ below
import pandas as pd
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def find_sum(df):
    sum=df['price'].aggregate('sum')
    return sum
