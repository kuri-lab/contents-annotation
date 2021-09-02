from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from models.database import Base
from datetime import datetime


class ImpressionContent(Base):
    __tablename__ = 'impressioncontents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reference1 = Column(String)
    reference2 = Column(String)
    target = Column(String)
    impression = Column(Float)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, reference1=None, reference2=None, target=None,impression=None, date=None):
        self.name = name
        self.reference1 = reference1
        self.reference2 = reference2
        self.target = target
        # 中心を０としている。マイナスがreference1でプラスがreference2
        self.impression = impression
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)

#以下を追加
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)
