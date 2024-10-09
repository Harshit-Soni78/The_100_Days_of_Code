# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# #  convert to dict.
# data_to_dict = data.to_dict()
# print(data_to_dict)
#
# # convert to list
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # get average
# print(sum(temp_list)/len(temp_list))
# print(data['temp'].mean())
#
# # get max
# print(data['temp'].max())
# print(data.condition.max())

# get data in row
# print(data[data.temp == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp * 9/5 + 32
# print(monday_temp)

# create a dataframe
data_dict = {
    "student": ["Any","Harshit","Pinky"],
    "scores": [76,96,98]
}
data = pandas.DataFrame(data_dict)

# saving the dataframe to a new csv file
data.to_csv("new_data.csv")
print(data)
