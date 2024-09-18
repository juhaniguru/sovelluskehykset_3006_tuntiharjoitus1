import mysql


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
                print("##############usrs", users)


                return users