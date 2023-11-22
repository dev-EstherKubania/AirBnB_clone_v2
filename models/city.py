#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = Column(String(60) ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", cascade"all, delete", backref="city")
