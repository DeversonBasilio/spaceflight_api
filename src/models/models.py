import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from sqlalchemy.sql.schema import ForeignKey

import config.database as _database

class Article(_database.Base):
    __tablename__ = 'articles'
    id = _sql.Column(_sql.Integer, primary_key = True)
    featured = _sql.Column(_sql.Boolean,default=False)
    title = _sql.Column(_sql.String(255))
    url   = _sql.Column(_sql.String(255)) 
    imageUrl = _sql.Column(_sql.String(255))
    newsSite = _sql.Column(_sql.String(255))
    summary = _sql.Column(_sql.String(255))
    publishedAt = _sql.Column(_sql.String(255)) 
    launches = _orm.relationship("Launche", back_populates="_article", cascade="all, delete-orphan")
    events = _orm.relationship("Event", back_populates="_article", cascade="all, delete-orphan")


class Launche(_database.Base):
    __tablename__ = 'launches'
    id = _sql.Column(_sql.String(255), primary_key=True)
    provider = _sql.Column(_sql.String(255))
    article_id = _sql.Column(_sql.Integer, _sql.ForeignKey('articles.id',ondelete='CASCADE'))
        
    _article = _orm.relationship("Article", back_populates="launches")

    
class Event(_database.Base):
    __tablename__ = 'events'
    id = _sql.Column(_sql.Integer,primary_key=True)
    provider = _sql.Column(_sql.String(255))
    article_id = _sql.Column(_sql.Integer, _sql.ForeignKey('articles.id',ondelete='CASCADE'), primary_key=True)

    _article = _orm.relationship("Article", back_populates="events")