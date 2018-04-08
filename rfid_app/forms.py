from flask_wtf import FlaskForm
from wtforms import SelectField
from rfid_app.models import Bus


class BusNumber(FlaskForm):
    """."""
    # import pdb; pdb.set_trace()
    buses = Bus.query.all()
    bus_number = SelectField('Bus Numbers:', choices=[(buses, buses)])
