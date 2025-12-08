#Q1: A
#Q2: False
#Q3: exponent, **
#Q4: 21, 20, 12
#Q5: B
#Q6: try, result, except
#Q7: python, PYTHON!!
#Q8: 
def calculate_product(value1, value2):
    total = value1 * value2
    print("The product is:", total)
    return total

output = calculate_product(5, 6)
print(output)
#Q9: A
#Q10: Not multiple of three, Multiple of three
#Q11: True
#Q12: split, upper
#Q13: 
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))
print(reverse_string("Python"))
print(reverse_string("a"))
#Q14: Test,Test,Test, Code,Code, Hi,Hi
#Q15: already working
#Q16: C
#Q17: lower, not, return
#Q18: 
def categorize_temperature(temp):
    if temp < -50 or temp > 50:
        return "Invalid"
    elif temp < 0:
        return "Freezing"
    elif temp <= 15:
        return "Cold"
    elif temp <= 25:
        return "Mild"
    elif temp <= 35:
        return "Warm"
    else:
        return "Hot"

print(categorize_temperature(-5))
print(categorize_temperature(20))
print(categorize_temperature(100))
#Q19: 
def format_number(value, precision=2):
    return f"{value:.{precision}f}"

print(format_number(123.4567, 3))
print(format_number(99.5))
print(format_number(7, 0))
#Q20: 
def validate_username(username):
    if len(username) < 3 or len(username) > 20:
        return False

    if not username[0].isalpha():
        return False

    for char in username:
        if not (char.isalnum() or char == '_'):
            return False

    return True

print(validate_username("user_123"))
print(validate_username("123user"))
print(validate_username("a"))
print(validate_username("very_long_username_here"))