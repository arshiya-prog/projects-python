def life_in_weeks(age):
    years_left = 90 - age
    months_left = years_left * 12
    weeks_left = months_left * 4
    return weeks_left

age = int(input("What's you age right now? "))
weeks_left = life_in_weeks(age)

print(f"You have {weeks_left} weeks left.")