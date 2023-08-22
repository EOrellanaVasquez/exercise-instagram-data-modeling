import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    secondname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True ,nullable=False)
    follower = relationship('Follower', uselist=False, backref="user")
    post = relationship('Post', uselist=False, backref="user")
    coment = relationship('Coment', uselist=False, backref="user")



class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer,ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer,ForeignKey('user.id'), primary_key=True)

 


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    media = relationship('Media', uselist=False, backref="post")
    coment = relationship('Coment', uselist=False, backref="post")
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


    
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    url = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {}
    
 ## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
