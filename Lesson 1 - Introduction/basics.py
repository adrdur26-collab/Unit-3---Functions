# # Defining a function
# def function_name():
#     pass
# # Calling a function
# function_name()

# def print_header():
#     print("="*20)
#     print("Student Report")
#     print("="*20)

# print_header()

# def draw_square():
#     # print("*****")
#     # print("*****")
#     # print("*****")
#     # print("*****")
#     # print("*****")
#     for i in range(5):
#         print("*****")

# draw_square()

# def morning_routine():
#     print("Morning Routine")
#     print("Brush Teeth")
#     print("Shower")
#     print("Do Hair")

# def school_schedule():
#     print("School Schedule")
#     print("Period 1 - Calculus")
#     print("Period 2 - Health")
#     print("Period 3 - Biology")

# def after_school():
#     print("After School Routine")
#     print("Go to Gym")
#     print("Do Homework")
#     print("Eat Dinner")

# def daily_routine():
#     morning_routine()
#     print()
#     school_schedule()
#     print()
#     after_school()

# daily_routine()

def calc_area_rect(w,l):
    area = w * l
    # print(area)
    print(f"Area of {w}{l}{area}")
calc_area_rect(5,10)