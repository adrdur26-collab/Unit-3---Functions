# def safe_level_up(xp, hours_studied):
#     try:
#         return xp // hours_studied
#     except ZeroDivisionError: 
#         print("No grind, no glory!")
#         return xp // 10
    
# print(safe_level_up(1000, 5))
# print(safe_level_up(500, 0))
# print(safe_level_up(750, 3))

# def activate_knowledge_crystal(code):
#     try:
#         return int(code)
#     except ValueError:
#         return 1
#     finally:
#         print("Crystal energy surge!")

# print(activate_knowledge_crystal("42"))
# print(activate_knowledge_crystal("magic"))
# print(activate_knowledge_crystal("999"))

def join_study_squad(members):
    if members == '':
        print("Squad disbanded :(")
        return 0
    count = 1
    found_non_separator = False
    for char in members:
        if char == ',':
            count += 1
        else:
            found_non_separator = True
    
    if not found_non_separator:
        print("Squad disbanded :(")
        return 0
    
    return count

print(join_study_squad("Alice,Bob,Charlie"))
print(join_study_squad(",,,"))
print(join_study_squad(""))
