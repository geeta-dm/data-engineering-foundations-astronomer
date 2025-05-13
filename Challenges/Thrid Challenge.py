#Question 
#Write an Text Message to a File and Read it Back
#INPUT: "Welcome to Linkled Learning"
#OUTPUT: "Welcome to Linkled Learning"


#Code Answer

# Python code​​​​​​‌‌​‌​​‌‌​‌‌​‌​​​‌​‌‌‌‌​‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def read_file(text):
    with open("example.txt",mode='w') as file:
        file.write(text)
    with open("example.txt",mode='r') as file:
        result=file.read()
    return result