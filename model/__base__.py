from sqlalchemy.ext.declarative import declarative_base


class _BaseModel(object):

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d


BaseModel = declarative_base(cls=_BaseModel)

