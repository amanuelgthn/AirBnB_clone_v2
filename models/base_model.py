#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import os
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey


HBNB_ENV = os.environ.get('HBNB_ENV', 'dev')
HBNB_MYSQL_USER = os.environ.get('HBNB_MYSQL_USER', 'hbnb_dev')
HBNB_MYSQL_PWD = os.environ.get('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
HBNB_MYSQL_HOST = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
HBNB_MYSQL_DB = os.environ.get('HBNB_MYSQL_DB', 'hbnb_dev_db')

if models.type_storage == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if models.type_storage == "db":
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, time_format)
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary = self.__dict__.copy()
        if "created_at" in dictionary:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary:
            dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Deletes the instance from the database"""
        from models import storage
        storage.delete(self)
        storage.save()
