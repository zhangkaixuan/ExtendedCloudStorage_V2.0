# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from db_connection import transactional

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    '''
    +-----------+------------------+------+-----+---------+----------------+
    | Field     | Type             | Null | Key | Default | Extra          |
    +-----------+------------------+------+-----+---------+----------------+
    | id        | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name      | varchar(255)     | NO   |     | NULL    |                |
    | pass      | varchar(255)     | NO   |     | NULL    |                |
    | email     | varchar(255)     | NO   |     | NULL    |                |
    | is_active | tinyint(1)       | NO   |     | NULL    |                |
    | is_reg    | tinyint(1)       | NO   |     | 1       |                |
    | created   | datetime         | NO   |     | NULL    |                |
    | modified  | datetime         | NO   |     | NULL    |                |
    +-----------+------------------+------+-----+---------+----------------+
    '''
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    password = Column('pass', String, nullable=False)
    email = Column('email', String, nullable=False)
    is_active = Column('is_active', Integer, nullable=False)
    is_reg = Column('is_reg', Integer, nullable=False, default=1)
    created = Column('created', DateTime, nullable=False)
    modified = Column('modified', DateTime, nullable=False)


    def __init__(self, name, password, email, is_active, created, modified, is_reg=1):
        self.name = name
        self.password = password
        self.email = email
        self.is_active = is_active
        self.is_reg = is_reg
        self.created = created
        self.modified = modified

    def __repr__(self):
        return '{"id":"%s", "name":"%s", "password":"%s", "email":"%s", "is_active":"%s", "is_reg":"%s", "created":' \
               '"%s", "modified":"%s"}' % (self.id, self.name, self.password, self.email, self.is_active, self.is_reg,
                                           self.created, self.modified)


class UserLogic(object):
    def __init__(self):
        pass

    @transactional
    def add_data(self, session, **kwargs):
        create_record = User(**kwargs)
        print session.add(create_record)

    @transactional
    def delete_data_by_id(self, session, **kwargs):
        idx = kwargs.get('id','')
        delete_record = session.query(User).filter_by(id=idx).one()
        session.delete(delete_record)

    @transactional
    def update_data_by_id(self, session, **kwargs):
        idx = kwargs.get('id','')
        if idx != '':
            kwargs.pop('id')
            session.query(User).filter_by(id=idx).update(kwargs)

    @transactional
    def get_by_kwargs(self, session, **kwargs):
        return session.query(User).filter_by(**kwargs).all()

if __name__ == '__main__':
    userOpr = UserLogic()
    kwargs = {}
    print "测试：查询user表所有的记录"
    print userOpr.get_by_kwargs(**kwargs)