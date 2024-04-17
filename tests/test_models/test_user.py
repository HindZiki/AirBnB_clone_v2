#!/usr/bin/python3
"""test User module """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """test User module """

    def __init__(self, *args, **kwargs):
        """test User module """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email(self):
        """test User module """
        new = self.value()
        self.assertEqual((new.email), None)

    def test_password(self):
        """test User module """
        new = self.value()
        self.assertEqual((new.password), None)

    def test_first_name(self):
        """test User module """
        new = self.value()
        self.assertEqual((new.first_name), None)

    def test_last_name(self):
        """test User module """
        new = self.value()
        self.assertEqual((new.last_name), None)
