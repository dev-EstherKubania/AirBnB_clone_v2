#!/usr/bin/python3
"""Function that defines the DBStorage class."""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.base_model import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from os import environ as env


class DBStorage:
    """ Manages storage of hbnb models in a MySQL database."""
    __engine = None
    __session = None
    __clsdict = {
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
    }

    def __init__(self):
        """Initialize the DBStorage class."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                          env['HBNB_MYSQL_USER'],
                                          env['HBNB_MYSQL_PWD'],
                                          env['HBNB_MYSQL_HOST'],
                                          env['HBNB_MYSQL_DB']
                                      ), pool_pre_ping=True
                                )
        if env.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the database session."""
        d = {}
        cls = cls if not isinstance(cls, str) else self.__clsdict.get(cls)
        if cls:
            for obj in self.__session.query(cls):
                d["{}.{}".format(
                    cls.__name__, obj.id
                    )] = obj
                return (d)
            for k, cls in self.__clsdict.items():
                for obj in self.__session.query(cls):
                    d["{}.{}".format(cls.__name__, obj.id)] = obj
        return (d)

    def new(self, obj):
        """Add an object to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all of the changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.remove()
