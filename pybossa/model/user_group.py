from sqlalchemy import Integer, Table, Text, Unicode
from sqlalchemy.schema import Column
from sqlalchemy.orm import relationship

from pybossa.core import db
from pybossa.model import make_timestamp


user_group_association = Table('user_group_association', db.Metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('group_id', Integer, ForeignKey('user_group.id'))
)

project_group_association = Table('project_group_association', db.Metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('group_id', Integer, ForeignKey('user_group.id'))
)


class UserGroup(db.Model):
    
    __tablename__ = 'user_group'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=254), nullable=False)
    created = Column(Text, default=make_timestamp)

    users = relationship('User', secondary=user_group_association,
                         backref='groups')
    projects = relationship('Project', secondary=project_group_association,
                            backref='groups')
