# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

from ecs.db.user_model import UserLogic

userDAO = UserLogic()


def auth(name, password):
    kwargs = {"name": name, "password": password}
    result = userDAO.get_by_kwargs(**kwargs)
    print name
    print password
    print result
    if len(result) != 0:
        return "OK"
    return "ERROR"

