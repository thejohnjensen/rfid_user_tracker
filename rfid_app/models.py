"""Create database models."""
from rfid_app import db
from datetime import datetime


class Student(db.Model):
    """Create model for students."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text())
    last_name = db.Column(db.Text())
    home_stop = db.Column(db.Text())
    school_stop = db.Column(db.Text())
    present = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        """Name of Student Object."""
        return '<Student {} {}>'.format(self.first_name, self.last_name)


class Bus(db.Model):
    """Model for buses."""

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)

    def __repr__(self):
        """Name of Bus Object."""
        return '<Bus {}>'.format(self.number)


class Route(db.Model):
    """Model for Route."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())

    def __repr__(self):
        """Name of Route Object."""
        return '<Route {}>'.format(self.name)


class TripHistory(db.Model):
    """Model containing trip history and where student exited the bus."""

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(
        db.Integer,
        db.ForeignKey('student.id'),
        nullable=False)
    trip_start = db.Column(db.DateTime)
    trip_end = db.Column(db.DateTime)
    bus_stop = db.Column(db.Text())