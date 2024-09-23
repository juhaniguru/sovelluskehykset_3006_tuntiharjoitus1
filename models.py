import mysql


class Vehicle:
    def __init__(self, _id, make, model):
        self.id = _id
        self.make = make
        self.model = model

    @staticmethod
    def get_all():
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM vehicles")
                vehicles = cur.fetchall()
                vehicle_list = []
                for v in vehicles:
                    vehicle_list.append(Vehicle(v['id'], v['make'], v['model']))
                return vehicle_list

    @staticmethod
    def list_to_json(vehicle_list):
        vehicles_json_list = []
        for vehicle in vehicle_list:
            vehicles_json_list.append(vehicle.to_json())
        return vehicles_json_list

    def to_json(self):
        return {'id': self.id, 'make': self.make, 'model': self.model}


class User:
    def __init__(self, _id, firstname, lastname, username):
        self.id = _id
        self.firstname = firstname
        self.lastname = lastname
        self.username = username

    @staticmethod
    def get_all():
        with mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="") as con:
            with con.cursor(dictionary=True) as cur:
                cur.execute("SELECT * FROM users")
                users = cur.fetchall()
                users_list = []
                for u in users:
                    user = User(u['id'], u['firstname'], u['lastname'], u['username'])
                    users_list.append(user)

                return users_list

    def to_json(self):
        return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname,
                'username': self.username}

    @staticmethod
    def list_to_json(users_list):
        json_list = []
        for u in users_list:
            json_list.append(u.to_json())

        return json_list
