# Simple Grade Calculator

# it will take the input form the user (marks in percentage)
marks = int(input("Enter Your Percentage:")) 

# if conditional statements are used
# if marks equal or greater than 90, then this statement will execute
if marks >= 90:
    print(marks, ".You got A grade")
    
# if marks equal or greater than 80 and less than 90, then this statement will execute
elif marks >= 80 and marks < 90:
    print(marks, ".You got B+ grade")
    
# if marks equal or greater than 70 and less than 80, then this statement will execute
elif marks >= 70 and marks < 80:
    print(marks, ".You got B grade")

# if marks equal or greater than 60 and less than 70, then this statement will execute  
elif marks >= 60 and marks < 70:
    print(marks, ".You got C+ grade")
    
# if marks equal or greater than 50 and less than 60, then this statement will execute  
elif marks >= 50 and marks < 60:
    print(marks, ".You got C grade")
    
# if marks less than 50, then this statement will execute
elif marks < 50:
    print(marks, ".You got F grade")
    
# if user enters a wrong input, then this statement will execute   
else:
    print("Some went wrong! Invalid Arguments")