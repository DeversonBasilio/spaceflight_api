import config.database as _database
import sqlalchemy.orm as _orm

import models.models as _models
import schemas.schemas as _schemas

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_articles(db:_orm.Session, skip:int, limit:int):
    return db.query(_models.Article).offset(skip).limit(limit).all()

def add_articles(db: _orm.Session,article: _schemas.ArticleCreate):
    db_article = _models.Article(
        id = article.id,
        featured = article.featured,
        title = article.title,
        url = article.url,
        imageUrl = article.imageUrl,
        newsSite = article.newsSite,
        summary  =article.summary,
        publishedAt = article.publishedAt
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_article(db = _orm.Session,article_id=int):
    return db.query(_models.Article).filter(_models.Article.id == article_id).first()

def remove_article(db = _orm.Session,article_id=int):
    rm_article = db.query(_models.Article).filter(_models.Article.id == article_id).first()
    db.delete(rm_article)
    db.commit()

def put_article(db = _orm.Session, article = _schemas.ArticleCreate, article_id = int):

    old_article = get_article(db=db,article_id=article_id)

    old_article.featured = article.featured
    old_article.title = article.title
    old_article.url = article.url
    old_article.imageUrl = article.imageUrl
    old_article.newsSite = article.newsSite
    old_article.summary = article.summary
    old_article.publishedAt = article.publishedAt

    db.add(old_article)
    db.commit()
    db.refresh(old_article)