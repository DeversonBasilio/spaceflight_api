import pydantic as _pydantic
from typing import List, Optional


### LAUNCHES
class _LauncheBase(_pydantic.BaseModel):
    id:str
    provider:str
    article_id: int

class LauncheCreate(_LauncheBase):
    pass

class Launche(_LauncheBase):
    id:str
    provider:str
    article_id: int

    class Config:
        orm_mode = True

    


### EVENTS
class _EventBase(_pydantic.BaseModel):
    id:int
    provider:str
    article_id: int

class EventCreate(_EventBase):
    pass

class Event(_EventBase):
    id:int
    provider:str
    article_id: int
        
    class Config:
        orm_mode = True


### Article
class _ArticleBase(_pydantic.BaseModel):
    id:int
    featured:bool
    title:str
    url:str
    imageUrl:str
    newsSite:str
    summary:str
    publishedAt: str
    

class ArticleCreate(_ArticleBase):
    pass

class Article(_ArticleBase):    
    id:int
    featured:bool
    title:str
    url:str
    imageUrl:str
    newsSite:str
    summary:str
    publishedAt: str
    launches : Optional[List[Launche]] = []
    events: Optional[List[Event]] = []
        
    class Config:
        orm_mode = True