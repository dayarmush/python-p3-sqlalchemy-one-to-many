from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Game(Base):

    __tablename__ = 'games'

    id = Column(Integer(), primary_key = True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review', backref='game', cascade='all, delete-orphan')

    def __repr__(self):
        return f'Game(ID: {self.id}, Title: {self.title}, Genre: {self.genre}, Platform: {self.platform} Price: {self.price})'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key = True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))


    def __repr__(self) -> str:
        return f'Review(ID: {self.id}, Score: {self.score}, Comments: {self.comment}, Game ID: {self.game_id})'
