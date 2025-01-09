import json

from api.models.base import Base

DEVICES = []

class Device(Base):

    def __init__(self, root_path, is_debug=False):
        self.data_path = root_path + "devices.json"
        self.load(is_debug)

    def get_devices(self):
        return self.data
    
    def get_device(self, device_id):
        for x in self.data:
            if x["id"] == device_id:
                return x
        return None
    
    def add_device(self, device):
        device["created_at"] = self.get_timestamp()
        device["updated_at"] = self.get_timestamp()
        self.data.append(device)
        self.save()
     
    def update_device(self, device_id, device):
        device = self.get_device(device_id)
        device["updated_at"] = self.get_timestamp()
        device.update(device)
        self.save()
    
    def remove_device(self, device_id):
        device = self.get_device(device_id)
        self.data.remove(device)
        self.save()
    
    def load(self, is_debug):
        if is_debug:
            self.data = DEVICES
        else:
            f = open(self.data_path, "r")
            self.data = json.load(f)
            f.close()
    
    def save(self):
        f = open(self.data_path, "w")
        json.dump(self.data, f)
        f.close()
