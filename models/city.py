#!/usr/bin/python3

"""Define a class called City"""

from models.base_model import BaseModel


class City(BaseModel):

    """
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.

    """
    state_id = ""
    name = ""
