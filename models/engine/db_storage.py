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
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == 'test':
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
        """
        save all the changes made in the session
        """
        self.__session.commit()
        
    def delete(self, obj=None):
        if obj is not None:
             self.__session.delete(obj)

    
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        calling remove() method on the privagte session attribute
        """
        self.__session.remove()