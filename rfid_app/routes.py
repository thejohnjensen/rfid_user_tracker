"""Handle view function routing."""
from flask import render_template, request, redirect, url_for
from rfid_app import app, db, Config
import pandas as pd
from rfid_app.models import Bus, BusStop
from urllib.parse import urlparse, parse_qs


conn_str = Config.SQLALCHEMY_DATABASE_URI


@app.route('/', methods=['GET', 'POST'])
def index():
    """Home view route, shows table of all students and bus info."""
    if request.method == 'POST':
        bus_number = request.form['bus_number']
        return redirect(url_for('bus_stops', number=bus_number))

    data = pd.read_sql('SELECT students.first_name, students.last_name, students.present, \
                bus_stops.name AS bus_stop, routes.name AS route_name, buses.number AS bus_number \
                FROM bus_stops, bus_stop_route, students, routes, buses, bus_route \
                WHERE students.home_stop_id=bus_stop_route.stop_id \
                AND students.home_stop_id=bus_stops.id \
                AND bus_stop_route.route_id=routes.id \
                AND bus_route.bus_id=buses.id \
                AND bus_stop_route.route_id=bus_route.route_id', con=conn_str)

    buses = Bus.query.all()

    return render_template('index.html', data=data.to_html(), buses=buses)


@app.route('/bus/<number>', methods=['GET', 'POST'])
def bus_stops(number):
    """Render all stops and students for the selected bus number."""
    if request.method == 'POST':
        bus_stop = request.form['bus_stop']
        return redirect(url_for('bus_number_and_stop', number=number, stop=bus_stop))

    data = pd.read_sql(f'SELECT students.first_name, students.last_name, students.present, \
                bus_stops.name AS bus_stop, routes.name AS route_name, buses.number AS bus_number\
                FROM bus_stops, bus_stop_route, students, routes, buses, bus_route \
                WHERE students.home_stop_id=bus_stop_route.stop_id \
                AND students.home_stop_id=bus_stops.id \
                AND bus_stop_route.route_id=routes.id \
                AND bus_route.bus_id=buses.id \
                AND bus_stop_route.route_id=bus_route.route_id \
                AND buses.number={number}', con=conn_str)

    bus_stops = pd.read_sql(f'SELECT bus_stops.name AS bus_stop \
            FROM bus_stops, buses, bus_stop_route, bus_route \
            WHERE buses.number={number} \
            AND bus_stops.id=bus_stop_route.stop_id \
            AND bus_stop_route.route_id=bus_route.route_id \
            AND bus_route.bus_id=buses.id', con=conn_str)

    bus_stops_list = bus_stops['bus_stop'].tolist()
    bus = Bus.query.filter_by(number=number).first().number

    return render_template('bus_detail.html', data=data.to_html(),
                           bus=bus, stops=bus_stops_list)


@app.route('/bus/<number>/<stop>', methods=['GET'])
def bus_number_and_stop(number, stop):
    """Render table for bus number and selected stop."""
    stop_query = db.session.query(BusStop).filter_by(name=stop).first()
    stop_id = stop_query.id
    data = pd.read_sql(f'SELECT students.first_name, students.last_name, students.present, \
                bus_stops.name AS bus_stop, routes.name AS route_name, buses.number AS bus_number\
                FROM bus_stops, bus_stop_route, students, routes, buses, bus_route \
                WHERE students.home_stop_id=bus_stop_route.stop_id \
                AND students.home_stop_id=bus_stops.id \
                AND bus_stop_route.route_id=routes.id \
                AND bus_route.bus_id=buses.id \
                AND bus_stop_route.route_id=bus_route.route_id \
                AND buses.number={number} \
                AND bus_stops.id={stop_id}', con=conn_str)

    return render_template('stop_detail.html', data=data.to_html(), bus=number, stop=stop)
