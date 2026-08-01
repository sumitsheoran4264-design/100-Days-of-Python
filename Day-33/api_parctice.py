import requests

# #responce parcitce
# response = requests.get(url="http://api.open-notify.org/iss-now.json") # end point url

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (latitude, longitude)

# print(iss_position)


LATITUDE = 28.628738
LONGITUDE = 75.616526
parameters = {
    "lat": LATITUDE,
    "lng":LONGITUDE

}
 


with requests.get("https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400",params=parameters) as response:
    data = response.json()
    
