from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey
from sqlalchemy.ext import declarative
from sqlalchemy.orm import relationship

ModelBase = declarative.declarative_base()


class DictBase(object):
    attributes = []

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        d = {}
        for attr in self.__class__.attributes:
            d[attr] = getattr(self, attr)
        return d

    def __getitem__(self, key):
        return getattr(self, key)


class User(ModelBase, DictBase):
    __tablename__ = 'user'
    attributes = ['id', 'code']
    id = Column('id', Integer, primary_key=True)
    code = Column('code', String(length=36), unique=True, nullable=False)
    addresses = relationship("Address", backref="user")


class Address(ModelBase, DictBase):
    __tablename__ = 'address'
    attributes = ['id', 'user_id', 'address']
    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, ForeignKey('user.id'))
    address = Column('address', String(length=64), unique=True, nullable=False)
    #user = relationship("User", backref="address")


class Transaction(ModelBase, DictBase):
    __tablename__ = 'transaction'
    attributes = ['id', 'source', 'destination', 'value']
    id = Column('id', Integer, primary_key=True)
    source = Column('source', String(64))
    destination = Column('destination', String(64), nullable=False)
    value = Column('value', Float, nullable=False)