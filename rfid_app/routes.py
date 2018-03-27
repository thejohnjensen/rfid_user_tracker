from rfid_app import app


@app.route('/')
def index():
    return 'Home Page!'
