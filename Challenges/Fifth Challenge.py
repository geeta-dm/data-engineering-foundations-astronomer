#Question 
#Find the Sum of Array Elements Using Numpy
#INPUT: [[7, 17], [13, 19], [5,0]]
#OUTPUT: 45


#Code Answer

# Python code​​​​​​‌‌​‌​​‌‌​‌‌​‌​‌​​‌‌​​​​‌‌ below
# Use print("messages...") to debug your solution.
import numpy as np
show_expected_result = False
show_hints = False

def find_sum(numbers):
    result=np.sum(numbers)
    return result