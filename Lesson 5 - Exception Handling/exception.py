"""
Lesson 5: Exception Handling - Practice Exercises
"""
# Common exception types
# 1 Zero division error
# print(10/0) # ZeroDivisionError: division by zero

# 2 TypeError
# print(5 + "5") # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 3 ValueError
# print(int("5"))
# print(int("bt")) # ValueError: invalid literal for int() with base 10: 'bt'

# 4 NameError
# print(school) # NameError: name 'school' is not defined

# try:
#     result = 10 / 0
# except:
#     print("Oops! Can't divide by zero.")

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# except ValueError:
#     print("That's not a number!")

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# except ValueError:
#     print("That's not a number!")
# else:
#     print(f"Result: {result}")
# finally:
#     print("Operation Complete!")

# ==========================
# Practice 1: Safe Division
# Instructions: Create a function that divides two numbers safely
# ==========================

# def safe_divide(a, b):
#     try:
#         result = a / b
#         return result
#     # except:
#     #     print("An error occured!")
#     #     return 0
#     except ZeroDivisionError:
#         print("Warning: Division by Zero!")
#         return 0

# print(safe_divide(10, 2))
# print(safe_divide(10, 0))
# ==========================
# Practice 2: Safe Input
# Instructions: Create a function that safely gets an integer from user
# ==========================
def get_age():
    try:
        age = int(input("Enter age: "))
        return age
    except ValueError:
        print("Please enter a number!")
        return 0 
user_age = get_age()
print(f"You are {user_age} years old.")

# ==========================
# Challenge 1: Safe Calculator
# Instructions: Build a calculator that handles invalid input and division by zero
# ==========================



# ==========================
# Challenge 2: Grade Input Validator
# Instructions: Keep asking for a grade until a valid number between 0-100 is entered
# ==========================