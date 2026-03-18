'''Using basic file reading function'''
# with open('/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)

'''Using csv directly on Python'''
# import csv

# with open('/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     # data = list(data)
#     temperatures = []

#     # for row in data[1:]:
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

'''Using Pandas'''
# Using pandas is really easy and fast. We don't have to open the file to read it and so on...
import pandas

data = pandas.read_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# Calculating average
# Not using series method
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp, 2))

# Using series method
# average = data.temp.mean()
# print(f"Mean: {average}")

# median = data["temp"].median()
# print(f"Median: {median}")

# mode = data["temp"].mode()
# print(f"Mode: {mode}")

# maximum = data["temp"].max()
# print(f"Maximum: {maximum}")

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# farenheit_temp = (monday_temp*(9/5))+32
# print(monday.value_counts())

# data_dict = {
#     "names": ["Johan", "Eren", "Benedict", "George"],
#     "scores": [100, 87, 76, 96]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/data.csv")
# print(data)

data = pandas.read_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260314.csv")
# print(data.columns)

gray_total = len(data[data['Primary Fur Color'] == "Gray"])
red_total = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_total = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_total, red_total, black_total]
}

color_df = pandas.DataFrame(color_dict)

color_df.to_csv("/Users/arshiya/Desktop/Coding/Python/projects-python/day-25/squirrel_count.csv")