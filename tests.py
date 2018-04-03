import unittest
from rfid_app import app, db
import rfid_app.models as models


class StudentModelCase(unittest.TestCase):
    """Class to test the student model."""

    def setUp(self):
        """Set up database."""
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/rfid_app_test'
        db.create_all()

    def tearDown(self):
        """Clean up DB."""
        # db.session.remove()
        # db.drop_all()

    def test_add_student(self):
        """Test that student can be created."""
        student = models.Student(first_name='sue', last_name='test')
        print(student)
        db.session.add(student)
        db.session.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)