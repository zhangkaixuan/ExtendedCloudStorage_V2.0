# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import ConfigParser


def getConn():
    dbConfig = ConfigParser.ConfigParser()
    dbConfig.read("/etc/ecs/ecs.config")

    dbType = dbConfig.get("DB", "DB_TYPE")
    dbUrl = dbConfig.get("DB", "DB_URL")
    dbName = dbConfig.get("DB", "DB_NAME")
    dbUser = dbConfig.get("DB", "DB_USER")
    dbPassword = dbConfig.get("DB", "DB_PW")

    if dbType == 'mysql':
        dbConnectionString = dbType + '+mysqldb://' + dbUser + ':' + dbPassword + '@' + dbUrl + '/' + dbName
        engine = create_engine(dbConnectionString)
        session = scoped_session(sessionmaker(bind=engine))
        return session()


def transactional(fn):
    def transact(self, **args):
        session = getConn()
        try:
            if fn.__name__ == 'get_by_kwargs':
                return fn(self, session, **args)
            else:
                fn(self, session, **args)
            session.commit()
        except Exception, e:
            print e
            session.rollback()
            raise

    transact.__name__ = fn.__name__
    return transact