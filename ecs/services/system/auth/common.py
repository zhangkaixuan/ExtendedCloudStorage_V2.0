# -*- coding: utf-8 -*-
__author__ = 'zhangkaixuan'

from ecs.db.user_model import UserLogic
from ecs.util.tools import decrypt, md5

userDAO = UserLogic()


def auth(name, password):
    realname = decrypt(10, name)
    print "user:" + name
    print "password:" + password
    kwargs = {"name": realname}
    result = userDAO.get_by_kwargs(**kwargs)

    if not result:
        return "no such user"

    else:
        print result
        if password == md5(result[0].password):
            return "OK"
        else:
            return "password error"




