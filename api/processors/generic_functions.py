import json
from datetime import datetime

DATA = []


class Generic_functions():
    def __init__(self, root_path, own_path, is_debug=False):
        self.data_path = root_path + own_path
        self.load(is_debug)
    
    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"
    
    def get_data(self):
        return self.data
    
    def get_data_by_ID(self, data_id):
        for x in self.data:
            if x["id"] == data_id:
                return x
        return None
    
    def add_data(self, data):
        data["created_at"] = self.get_timestamp()
        data["updated_at"] = self.get_timestamp()
        self.data.append(data)
    
    def update_data(self, data_id, data):
        data["updated_at"] = self.get_timestamp()
        for i in range(len(self.data)):
            if self.data[i]["id"] == data_id:
                self.data[i] = data
                break
    
    def remove_data(self, data_id):
        for x in self.data:
            if x["id"] == data_id:
                self.data.remove(x)
    
    def load(self, is_debug):
        if is_debug:
            self.data = []
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()
    
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
