#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.place import Place
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if models.type_storage == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'))
    else:
        state_id = ""
        name = ""
    
    
    def __init__(self, *args, **kwargs):
        """
        Initializer for City
        """
        super().__init__(*args, **kwargs)
