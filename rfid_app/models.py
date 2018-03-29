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
        """Name of object."""
        return '<Student {} {}>'.format(self.first_name, self.last_name)