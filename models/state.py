#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.type_storage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """Initializer for State"""
        super().__init__(*args, **kwargs)

    if models.type_storage != "db":
        @property
        def cities(self):
            """
            public getter method cities to return list of CIty objects
            from storage linked to the current state
            """
            cities = []
            dict_cities = models.storage.all(City)
            for city in dict_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
