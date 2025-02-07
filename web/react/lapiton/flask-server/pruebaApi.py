import json
from urllib import request as request_api
import re

response = request_api.urlopen("https://superheroapi.com/api/7693742abd0d2968a66bc4d38f33db24/1")
data = response.read()
data = data.decode("utf-8")



