#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer

class Review(BaseModel):
    """ Review classto store review information """
    if models.type_storage == "db":
        __tablename__ = "reviews"
        place_id = Column(Integer, ForeignKey("places.id"), nullable=False)
        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
        
    def __init__(self, *args, **kwargs):
        """Intializer for Review module"""
        super().__init__(*args, **kwargs)
