#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jan 10 17:34:57 2023
@author: Jules Andretti
"""
print('Content-type: application/json\n')

import cgi
import json
import os
import pymysql
import sys

sys.path.insert(1, '/home/andrettj_SEV5204E/public_html/ws/lib') # Remplacer par votre login
import lib.wslib as wslib

log = 'andrettj_SEV5204E'
mdp = '60646N'
connection = wslib.connect(log,mdp)

httpData = wslib.returnHttpData()


accept = os.environ['HTTP_ACCEPT']
method=os.environ['REQUEST_METHOD']


loginMdp = os.environ['HTTP_X_AUTH'].split(':')
right = wslib.droit(connection,loginMdp)
if right == 'error':
    print(json.dumps({'code': 'WRONG_USER', 'text': 'No user found with the given login and password', 'data': None}))
    



if 'HTTP_ACCEPT' not in os.environ:
    return_value = {'code': 'MISSING_HEADER', 'text': 'the accept header should be provided in the http request', 'data': None}
elif os.environ['HTTP_ACCEPT'] != 'application/json':
    return_value = {'code': 'WRONG_HEADER', 'text': 'the accept header should be application/json', 'data': None}
elif method == 'POST':
    if not list(right.values())[0] in ["all","write"] :
        return_value = {'code': 'WRONG_RIGHT', 'text': 'you must have write/all rights', 'data': None}
    else:
        dest = httpData
        if dest:
            rep = wslib.PostRessource(dest,connection)
            return_value = rep
        else:
            return_value = {'code': 'MISSING_PARAMETERS', 'text': 'We do not received parameters', 'data': None}
elif method != 'GET':
    return_value = {'code': 'WRONG_METHOD', 'text': 'the method should be GET', 'data': None}
else:
    dest = httpData
    output = wslib.readRessource(dest,connection)
    if output:
        return_value= {'code': 'OK', 'text': 'the asked resource was successfully returned', 'data': output}
    else :
        return_value= {'code': 'WRONG_PARAMETER', 'text': 'the asked parameter is not in the db or missing parameter', 'data': None}
connection.close()

print(json.dumps(return_value))
