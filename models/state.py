#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import environ as env
from models.base_model import BaseModel, Base
from sqlachemy import Column, String, ForeignKey
from sqlachemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """
        Returns a list of City instances with state_id
        equals to the current State.id
        """
        var = models.storage.all()
        list = []
        for key in var:
            city = key.replace('.', '')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list.append(var[key])
        for elem in list:
            if (elem.state_id == self.id):
                results.append(elem)
        return (results)
