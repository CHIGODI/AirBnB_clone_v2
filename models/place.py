#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")
    p_amenities = relationship("Amenity",
                                   secondary=association_table,
                                   viewonly=False)

    @property
    def reviews(self):
        from . import storage
        from models.review import Review
        my_reviews = []
        reviews_only = storage.all(Review)
        for key, val in reviews_only.items():
            if val.place_id == self.id:
                my_reviews.append(val)
        return my_reviews

    @property
    def amenities(self):
        from . import storage
        from models.amenity import Amenity
        my_amenities = []
        amenities_only = storage.all(Amenity)
        for a_id in Place.amenity_ids:
            my_amenities.append(amenities_only[f"Amenity.{a_id}"])
        return my_amenities

    @amenities.setter
    def amenities(self, value):
        from . import storage
        from models.amenity import Amenity
        if value in storage.all(Amenity):
            Place.amenity_ids.append(value)
