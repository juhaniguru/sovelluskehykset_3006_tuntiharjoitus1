from flask import jsonify, render_template

import models


def get_all_vehicles_api():
    vehicles = models.Vehicle.get_all()
    return jsonify(models.Vehicle.list_to_json(vehicles))

def get_all_vehicles_html_page():
    vehicles = models.Vehicle.get_all()
    return render_template('vehicles/index.html', vehicles_param=vehicles)
