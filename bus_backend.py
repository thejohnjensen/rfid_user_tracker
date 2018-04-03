from rfid_app import app, db
from rfid_app.models import Student, Bus, Route, TripHistory, BusStop, bus_and_routes, bus_stops_and_routes


@app.shell_context_processor
def make_shell_context():
    """."""
    return {'db': db, 'Student': Student, 'Bus': Bus,
            'Route': Route, 'TripHistory': TripHistory, 'BusStop': BusStop,
            'bus_and_routes': bus_and_routes,
            'bus_stops_and_routes': bus_stops_and_routes}
