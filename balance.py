#!/usr/bin/python
# -*- coding: utf8 -*-
from hashlib import sha1, md5
from collections import OrderedDict
from urllib import urlencode
import hmac
import requests

#-------------------------------------------------------------------------------
#  Личные данные API и путь для обращения
#-------------------------------------------------------------------------------
api_key      = 'В личном кабинете zadarma.com -> API поле Key'
secret_key   = 'В личном кабинете zadarma.com -> API   Secret'
path         = '/v1/info/balance/'
data         = { 'format': 'json'}


#-------------------------------------------------------------------------------
#  Обработка и формирование авторизационной строки
#-------------------------------------------------------------------------------

od = OrderedDict(sorted(data.items()))
query_string = urlencode(od)
h = md5(query_string)
data = path + query_string + h.hexdigest() 
hashed = hmac.new(secret_key, data, sha1)
auth   = api_key + ':' + hashed.hexdigest().encode("base64")

#-------------------------------------------------------------------------------
#  Отправка запроса и получение ответа
#-------------------------------------------------------------------------------
headers = {'User-Agent': '-', 'Authorization': auth}
url = 'https://api.zadarma.com' + path + '?' + query_string;
r = requests.get(url, headers=headers)
print(r.text)
