# Capital = {
#     "Farnce": "Paris",
#     "Germany": "Barlin",
#     }

# #Nested List in Dictionary

# travel_log = {
#     "Farnce": [],
#     "Germany": ["Stuttgrat", "Berlin"],
# }

# print(travel_log["Germany"][1])

# #Nested list in list
# nested_list = ["A", "B",[ "C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "Farnce": {"num_times_visited": 8,
               "cities_vistied": ["Paris", "Lille", "Dijon"]
               },
    
    
    "Germany": ["Stuttgrat", "Berlin"],
}
print(travel_log["Germany"][0])