import random
import pandas
# count = 0
# name = "Aryan"

# new_list = [(i, count) for i in name]

# new_list = [(f"{name[i]}{i+1}") for i in range(5)]
# new_list = [(name[i], i+1) for i in range(5)]
# print(new_list)

# names = ["Arthur", "Leon", "Joel", "Michael", "Motu", "Ellie", "Trevor"]
# new_dict = {key:random.randint(1,100) for key in names}
new_dict = {"students": ["Arthur", "Leon", "Joel", "Michael"],
            "marks": [85, 93, 78, 69]}

new_dataframe = pandas.DataFrame(new_dict)
# print(new_dataframe)

# for (key, value) in new_dataframe.items():
#     print(key)
#     print()
#     print(value)

for (index, row) in new_dataframe.iterrows():
    print(index)
    print(row)

# passed_students = {key:value for (key, value) in new_dict.items() if value>60}
# print(new_dict)
# print(new_dict.items())
# print(passed_students)
# names_with_4_letters = []

# names_with_4_letters = [name.upper() for name in names if len(name) > 4]
# print(names_with_4_letters)

# for name in names:
#     if len(name) == 4:
#         names_with_4_letters.append(name)

# print(names_with_4_letters)