#!/usr/bin/python3
"""
DBStorage
"""


import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage():
    __engine = None
    __session = None
    classes_dict = {'User': User, 'State': State, 'City': City,
                    'Amenity': Amenity, 'Place': Place, 'Review': Review}

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),getenv('HBNB_MYSQL_DB'), pool_pre_ping=True))
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """converts query to a dict of objects"""
        objs = {}
        for clss in self.classes_dict:
            if cls is None or cls is self.classes_dict[clss] or cls is clss:
                objct = self.__session.query(self.classes_dict[clss]).all()
                for obj in objct:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        return objs

    def new(self, obj):
        """
        add obj to the current session
        """
        self.__session.add(obj)
    
    def save(self):
        """s
        ave all the changes made in the session
        """
        self.__session.commit()
        
    def delete(self, obj=None):
        if obj is not None:
             self.__session.delete(obj)
             self.__session.commit()
    
    def reload(self):
        """create all tables in the database(feature of SQLAlchemy)(WARNING:all classes 
        which inherits from Base must be imported before calling Base.metadata.create_all
        (self.__engine), create the current database session from the engine by a sessionmaker
        - the option expire_on_commit must be set to False and scopped_session to make the session thread-safe)
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        self.__session.expire_on_commit = False

    def close(self):
        """
        calling remove() method on the privagte session attribute
        """
        self.__session.remove()