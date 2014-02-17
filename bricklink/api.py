'''
    bricklink.api
    -------------

    A module providing access to the Bricklink API
'''

from rauth import OAuth1Service

class ApiClient:
    __attrs__ = ['consumer_key', 'consumer_secret']

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.service = OAuth1Service(name='bricklink',
                                     consumer_key=consumer_key,
                                     consumer_secret=consumer_secret,
                                     base_url='https://api.bricklink.com/api/store/v1/')

        self.session = self.service.get_session((access_token, access_token_secret))

    def get(self, params):
        pass