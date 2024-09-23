import mysql.connector
from flask import Flask, jsonify, render_template

from controllers import vehicles_controller

app = Flask(__name__)

app.add_url_rule('/api/vehicles', view_func=vehicles_controller.get_all_vehicles_api)
app.add_url_rule('/vehicles', view_func=vehicles_controller.get_all_vehicles_html_page)

if __name__ == '__main__':
    app.run()
