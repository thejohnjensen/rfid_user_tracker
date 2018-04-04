"""Create database models."""
from rfid_app import db
from datetime import datetime


bus_stops_and_routes = db.Table('bus_stop_route',
                                db.Column('stop_id',
                                          db.Integer,
                                          db.ForeignKey('bus_stops.id')),
                                db.Column('route_id',
                                          db.Integer,
                                          db.ForeignKey('routes.id')))


bus_and_routes = db.Table('bus_route',
                          db.Column('route_id',
                                    db.Integer,
                                    db.ForeignKey('routes.id')),
                          db.Column('bus_id',
                                    db.Integer,
                                    db.ForeignKey('buses.id')))


class Student(db.Model):
    """Create model for students."""

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    home_stop_id = db.Column(db.Integer, db.ForeignKey('bus_stops.id'))
    school_stop = db.Column(db.Text())
    present = db.Column(db.Boolean(), default=False)
    # ride = db.relationship(
    #     'trip_history',
    #     backref='student',
    #     lazy=True)

    def __repr__(self):
        """Name of Student Object."""
        return '<Student {} {}>'.format(self.first_name, self.last_name)


class Bus(db.Model):
    """Model for buses."""

    __tablename__ = 'buses'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

    def __repr__(self):
        """Name of Bus Object."""
        return '<Bus {}>'.format(self.number)


class Route(db.Model):
    """Model for Route."""

    __tablename__ = 'routes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())

    def __repr__(self):
        """Name of Route Object."""
        return '<Route {}>'.format(self.name)


class TripHistory(db.Model):
    """Model containing trip history and where student exited the bus."""

    __tablename__ = 'trip_history'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey('students.id'),
        nullable=False)
    trip_start = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)
    trip_end = db.Column(db.DateTime)
    bus_stop = db.Column(
        db.Integer,
        db.ForeignKey('bus_stops.id'))


class BusStop(db.Model):
    """Model for all bus stops."""

    __tablename__ = 'bus_stops'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())

    def __repr__(self):
        return '<BusStop {}>'.format(self.name)