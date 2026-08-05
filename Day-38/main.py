import requests
from datetime import datetime
API_KEY = "nix_live_fkbkvm75jRhN7bXYJRADUUN9mUIaLPWG"                                                                                       #https://app.100daysofpython.dev/services/nutrition/docs,  https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/edit?pli=1&gid=0#gid=0
APP_ID = "app_c7b350e64cb8403a9087ff02"
SHEET_ENDPOINT = "https://api.sheety.co/628a08ebaa678b9c0852c930cdf26b75/myWorkouts/workouts"
BASE_URL = "https://app.100daysofpython.dev"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
data = {
    'query': input("Tell me which exercise you did: ")
}


NUTRITION_ENDPOINT = f"{BASE_URL}/v1/nutrition/natural/exercise"

response = requests.post(url=NUTRITION_ENDPOINT, json=data, headers=headers)
data = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

nutrition_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
for exercise in data["exercises"]:

    sheet_input = {
        "workout":{
    'date': today_date,
    'time': now_time,
    'exercise': exercise['name'].title(),
    'duration': exercise['duration_min'],
    'calories': exercise['nf_calories']
}}
    
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_input)
    print(sheet_response.status_code)
    print(sheet_response.text)
