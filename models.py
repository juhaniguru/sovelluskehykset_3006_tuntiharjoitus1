import mysql


class Vehicle:
    def __init__(self, _id, make, model):
        self.id = _id
        self.make = make
        self.model = model



    @staticmethod
    def list_to_json(vehicle_list):
        vehicles_json_list = []
        for vehicle in vehicle_list:
            vehicles_json_list.append(vehicle.to_json())
        return vehicles_json_list

    def to_json(self):
        return {'id': self.id, 'make': self.make, 'model': self.model}



