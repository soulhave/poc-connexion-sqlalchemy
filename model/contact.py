from sqlalchemy import Column, Integer, String, Date
from model.__base__ import BaseModel


class Contact(BaseModel):
    __tablename__ = 'Contact'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    birthday = Column(Date)

    def __repr__(self):
        return "<User(id='%s', name='%s', birthday='%s')>" % \
               (self.id, self.name, self.birthday)

    @staticmethod
    def to_model(contact):
        return Contact(name=contact['name'],
                       birthday=contact['birthday'])
