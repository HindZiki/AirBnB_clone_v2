#!/usr/bin/python3
"""test Place module """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test Place module """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_user_id(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_city_id(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.city_id), None)

    def test_name(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.name), None)

    def test_number_bathrooms(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.number_bathrooms), None)

    def test_description(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.description), None)

    def test_max_guest(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.max_guest), None)

    def test_number_rooms(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.number_rooms), None)

    def test_price_by_night(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.price_by_night), None)

    def test_longitude(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_latitude(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.latitude), None)

    def test_amenity_ids(self):
        """test Place module """
        new = self.value()
        self.assertEqual((new.amenity_ids), [])
