import fastapi as _fastapi
import sqlalchemy.orm as _orm

from typing import List

import config.services as _services
import schemas.schemas as _schemas


app = _fastapi.FastAPI()

_services.create_database()

@app.get("/")
def raiz():
    return "Back-end Challenge 2021 🏅 - Space Flight News"

@app.get("/articles/",response_model=List[_schemas.Article])
def read_articles(skip:int=0,limit:int=10,db:_orm.Session = _fastapi.Depends(_services.get_db)):
    articles = _services.get_articles(db=db, skip=skip,limit=limit)
    return articles


@app.post("/articles/",response_model=_schemas.Article)
def create_article(article: _schemas.ArticleCreate, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.add_articles(db=db,article = article)

@app.get("/articles/{article_id}",response_model=_schemas.Article)
def read_article(article_id:int, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    db_article = _services.get_article(db=db,article_id=article_id)

    if db_article is None:
        raise _fastapi.HTTPException(status=404,detail="Artigo não encontrado!")

    return db_article

@app.delete("/articles/{article_id}")
def delete_article(article_id:int, db:_orm.Session = _fastapi.Depends(_services.get_db)):
    _services.remove_article(db=db,article_id=article_id)
    return "Deleted with Success"

@app.put("/articles/{article_id}")
def update_article( article_id:int, 
                    article: _schemas.Article,
                    db:_orm.Session = _fastapi.Depends(_services.get_db)
                ):
    return _services.put_article(db=db,article=article, article_id=article_id)
    