import requests

class Client():

    def __init__(self,url, method, type, header, data):
        self.url = url
        self.method = method
        self.type = type
        self.headers = header
        self.data = data





class Type:
    FORM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE = 5