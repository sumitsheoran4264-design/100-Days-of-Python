from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from config import API_KEY, BASE_URL



data_manager = DataManager("Day-40/data.json")
flight_search = FlightSearch()
notification_manager =  NotificationManager()

name = input("What is your name?: ").lower()
phone_num = input("What is your phone number?: ")
email = input("What is your email?: ")

#user_data 
user_data = {
    "name": name,
    "contact": phone_num,
    "email": email
}
data_manager.save_user(user=user_data)
data_manager.update_destination_data("delhi")