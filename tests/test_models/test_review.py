#!/usr/bin/python3
"""test Review module """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test Review module """

    def __init__(self, *args, **kwargs):
        """test Review module """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_user_id(self):
        """test Review module """
        new = self.value()
        self.assertEqual((new.user_id), None)

    def test_text(self):
        """test Review module """
        new = self.value()
        self.assertEqual((new.text), None)

    def test_place_id(self):
        """test Review module """
        new = self.value()
        self.assertEqual((new.place_id), None)
