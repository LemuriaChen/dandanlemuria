
import http.client
import hashlib
import urllib
import random
import json


class Trans:
    def __init__(self):
        self.app_id = None
        self.secret_key = None
        self.url = '/api/trans/vip/translate'

    def add_app_id(self, app_id):
        self.app_id = app_id

    def add_secret_key(self, secret_key):
        self.secret_key = secret_key

    def translate(self, query='', from_lang='auto', to_lang='zh'):

        assert self.app_id is not None and self.secret_key is not None, \
            'please add app id using \'add_app_id\' and add secret key using \'add_secret_key\''

        salt = random.randint(32768, 65536)
        sign = self.app_id + query + str(salt) + self.secret_key
        sign = hashlib.md5(sign.encode()).hexdigest()

        url = self.url + '?appid=' + self.app_id + '&q=' + urllib.parse.quote(
            query) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(
            salt) + '&sign=' + sign

        result, http_client = None, None

        try:
            http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
            http_client.request('GET', url)
            response = http_client.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
        except Exception as e:
            print(e)
        finally:
            if http_client:
                http_client.close()

        return result
