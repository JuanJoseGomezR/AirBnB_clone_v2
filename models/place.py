#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")


    if getenv('HBNB_TYPE_STORAGE') == 'db':

        amenities = relationship("Amenity",secondary="place_amenity",viewonly=False,)

        @property
        def reviews(self):
            '''reviews call relationship'''
            rev = []
            for review in self.reviews:
                if review.place_id == self.id:
                    rev.append[review]
            return reviews
    else:
        @property
        def reviews(self):
            myreviews = []
            for id, r in models.storage.all(Review).items():
                if self.id == r.place.id:
                    myreviews.append(r)
            return myreviews

        @property
        def amenities(self):
            myamenities = []
            for a in amenity_ids:
                if self.id == a.id:
                    myamenities.append(a)
            return myamenities

        @amenities.setter
        def amenities(self, amenity):
            if type(amenity).__name__ == 'Amenity':
                self.amenity_ids.append(amenity)
