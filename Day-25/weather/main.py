# with open("Day-25/weather_data.csv") as data_csv:
#     data = data_csv.readlines()
#     print(data)

# import csv
# with open("Day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     next(data)
#     temperature = []

#     for row in data:
#         temperature.append(int(row[1]))

#     print(temperature)


import pandas
data = pandas.read_csv("Day-25/weather/weather_data.csv")
data_t = data['temp']
# print(data_t)
# temp_max = data["temp"].max()


# # get data in column
print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max() ])

# data_c = data.condition
# print(data_c)



# monday = data[data.day == "Monday"]
# # print(monday)
# # print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)



# create a dataframe from scratch

# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [44, 34, 59]

# }
# data = pandas.DataFrame(data_dict)

# # print(data)
# data.to_csv("new_file.csv")


   