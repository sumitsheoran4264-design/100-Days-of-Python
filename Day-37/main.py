import requests


pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "sumitjaat"
TOKEN = "SumitSheoran"
ID = "graph1"
DATE = "20260804"

#Post

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#graph create
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float", 
    "color": "ichou"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# GOOGLE SEARCH = https://pixe.la/v1/users/sumitjaat/graphs/graph1.html


#pixel create
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

post_config = {
    "date": DATE, #yyyyMMDD
    "quantity": "3",
}

# response = requests.post(url=pixel_create_endpoint,json=post_config, headers=headers)
# print(response.text)
  
#update pixel 
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"

update_config = {
    "quantity": "5.6"
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)

# print(response.text)
#delete

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{DATE}"

response = requests.delete(url=delete_pixel_endpoint,headers=headers)

print(response.text)