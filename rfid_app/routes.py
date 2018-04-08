from flask import render_template, request, redirect
from rfid_app import app, db, Config
import pandas as pd
from rfid_app.models import Bus, BusStop
from urllib.parse import urlparse, parse_qs
from rfid_app.forms import BusNumber


conn_str = Config.SQLALCHEMY_DATABASE_URI


@app.route('/', methods=['GET', 'POST'])
def index():
    # import pdb; pdb.set_trace()
    print(request.path)
    if request.method == 'POST':
        pass

    form = BusNumber()
    data = pd.read_sql('SELECT students.first_name, students.last_name, students.present, \
                bus_stops.name AS bus_stop, routes.name AS route_name, buses.number AS bus_number\
                FROM bus_stops, bus_stop_route, students, routes, buses, bus_route \
                WHERE students.home_stop_id=bus_stop_route.stop_id \
                AND students.home_stop_id=bus_stops.id \
                AND bus_stop_route.route_id=routes.id \
                AND bus_route.bus_id=buses.id \
                AND bus_stop_route.route_id=bus_route.route_id', con=conn_str)
    buses = Bus.query.all()
    stops = BusStop.query.all()
    # import pdb; pdb.set_trace()
    return render_template('index.html', data=data.to_html(), buses=buses, stops=stops, form=form)


@app.route('/bus/', methods=['GET', 'POST'])
def bus_stops():
    # import pdb; pdb.set_trace()
    return "Hello"
