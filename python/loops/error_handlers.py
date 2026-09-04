try:
    # 1.risky code 
    number = int(input("Enter a divisior"))
    result = 10/number
except ZeroDivisionError:
    #runs only if zero division error occurs
    print("You cannot divide by zero")
except ValueError:
    # runs only if input cannot be turned into integer
    print("Please enter a valid number")
else:
    # runs only if the try block runs without any error
    print(f"success! The result is {result}")
finally:
    #always runs no matter what
    print("cleaning up resources")