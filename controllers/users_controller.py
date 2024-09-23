import mysql
from flask import jsonify

import models


def get_all_users():  # put application's code here

    users = models.User.get_all()
    return jsonify(models.User.list_to_json(users))
