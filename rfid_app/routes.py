from rfid_app import app
import pandas as pd
from rfid_app.models import Student

@app.route('/')
def index():
    return 'Home Page!'
