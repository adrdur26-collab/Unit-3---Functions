# def safe_multiply(x, y):
#     if isinstance(x,(int,float)) and isinstance(y,(int,float)):
#         return x * y
#     return 0

# print(safe_multiply(5, 3))
# print(safe_multiply(4, "a"))

def is_positive(value):
    try:
        return isinstance(value, (int,float)) and value > 0
    except:
        return False
    
print(is_positive(5))
print(is_positive(-3))
print(is_positive('hello'))

def safe_multiply(x, y):
    try:
        return x * y
    except TypeError:
        return 0
    
# Q2: -1

def is_positive(value):
    try:
        return isinstance(value, (int, float)) and value > 0
    except:
        return False

# Q4: Processing Complete 0

def format_message(code, text):
    try:
        return f"[{code}] {text}"
    except:
        return "[ERROR] invalid"

#Q6: Calculation done 16

def safe_average(a, b):
    try:
        return (a + b) / 2
    except ZeroDivisionError:
        return 0

#Q8: Process Complete 50.0

#Q9: 0