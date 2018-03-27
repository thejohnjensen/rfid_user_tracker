from setuptools import setup


setup(
    name='rfid_app',
    version='1.0',
    description='RFID card reader with database',
    author='John Jensen',
    py_modules=['bus_backend'],
    install_requires=[
        'flask-sqlalchemy',
        'flask-migrate'
    ],
    extras_require={
        'dev': [],
        'test': []
    }
)