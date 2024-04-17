#!/usr/bin/python3
"""City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test City module """

    def __init__(self, *args, **kwargs):
        """test City module """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test City module State id"""
        new = self.value()
        self.assertEqual((new.state_id), None)

    def test_name(self):
        """test City module name"""
        new = self.value()
        self.assertEqual((new.name), None)
