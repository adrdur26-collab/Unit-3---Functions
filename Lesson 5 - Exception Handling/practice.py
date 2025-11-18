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
