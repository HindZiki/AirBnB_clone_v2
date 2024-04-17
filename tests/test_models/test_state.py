#!/usr/bin/python3
"""test State module """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test State module """

    def __init__(self, *args, **kwargs):
        """test State module """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test State module """
        new = self.value()
        self.assertEqual((new.name), None)
