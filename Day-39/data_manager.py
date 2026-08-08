import json
class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path


    def get_destination_data(self):
        with open(self.file_path) as data_file:
            self.data = json.load(data_file)
            return self.data["destinations"]

    def get_user_data(self):
        with open(self.file_path) as data_file:
            self.user_data = json.load(data_file)
            return self.user_data["users"]
        

    def save_user(self, user):
        "This function save data in data file "
        
        with open(self.file_path) as user_data:
            data = json.load(user_data)
            data["users"].append(user)
        with open(self.file_path, mode="w") as user_data:
            json.dump(data, user_data, indent=4)

    
        

    def update_destination_data(self, destinations):
        with open(self.file_path) as data_file:
            data =json.load(data_file)
            data["destinations"] = destinations
        with open(self.file_path, mode="w") as data_file:
            json.dump(data, data_file, indent=4)

