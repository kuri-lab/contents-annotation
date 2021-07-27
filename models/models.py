from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from models.database import Base
from datetime import datetime


class ImpressionContent(Base):
    __tablename__ = 'impressioncontents'
    id = Column(Integer, primary_key=True)
    reference1 = Column(String)
    reference2 = Column(String)
    target = Column(String)
    ref1 = Column(Float)
    ref2 = Column(Float)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, reference1=None, reference2=None, target=None,ref1=None, ref2=None, date=None):
        self.reference1 = reference1
        self.reference2 = reference2
        self.target = target
        self.ref1 = ref1
        self.ref2 = ref2
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
