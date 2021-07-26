from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from models.database import Base
from datetime import datetime


class ImpressionContent(Base):
    __tablename__ = 'impressioncontents'
    id = Column(Integer, primary_key=True)
    ref1 = Column(Float)
    ref2 = Column(Float)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, ref1=None, ref2=None, date=None):
        self.ref1 = ref1
        self.ref2 = ref2
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
