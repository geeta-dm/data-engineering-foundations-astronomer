#Question 
#Find the Smallest number in a List
#INPUT: [2,5,20,30,56]
#OUTPUT: 2


#Code Answer
# Python code​​​​​​‌‌​‌​​‌‌​​‌‌​‌​​‌‌​‌‌​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def find_smallest(numbers):
    f=numbers[0]
    small=0
    for i in range(1,len(numbers)):
        if f>numbers[i]:
            small=small+numbers[i]
    return small