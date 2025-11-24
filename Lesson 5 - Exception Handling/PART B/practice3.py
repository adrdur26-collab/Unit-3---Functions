# Raising Exceptions - Making your code say "no"!

# def set_volume(level):
#     """Set volume level (0-100)"""
#     if level < 0:
#         raise ValueError("Volume cannot be negative!")
#     if level > 100:
#         raise ValueError("Volume cannot exceed 100!")
#     volume = level
#     print(f"Volume set to {volume}")

# try:
#     set_volume(50) # works fine
#     set_volume(-10) # raises value error
# except ValueError as error:
#     print(f"Error: {error}")
"""
Which exception should I raise?
ValueError - Onvalid Values (wrong number, wrong format)
TypeError - Wrong data type provided
RuntimeError - General Error in our function
"""

def create_username(name):
    """
    Create a valid username.
    Rules:
        - Must be at least 3 characters
        - Can not be more than 20 character
        - Cannot be empty
    """
    # Checking if empty
    if name == "" or not name:
        raise ValueError("Username cannot be empty!")
    # Check mininimum length
    if len(name) < 3:
        raise ValueError("Username must be at least 3 characters!")
    if len(name) > 20:
        raise ValueError("Username cannot exceed 20 characters!")
    
    # All checks passed
    username = name.lower()
    print(f"Username created: {username}")
    return username


# Test valid username
try:
    user = create_username("GamerPro")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")
# Test too short
try:
    user = create_username("ab")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")
try:
    user = create_username("")
    print(f"Success: {user}")
except ValueError as e:
    print(f"Error: {e}")


def divide(a,b):
    """Divide two numbers safely"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    result = a / b
    return result

try:
    print(divide(10,2))
    print(divide(10,0))
except ValueError as e:
    print(f"Error: {e}")