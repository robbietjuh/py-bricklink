'''
    bricklink.api
    -------------

    A module providing access to the Bricklink API
'''

from exceptions import *

from rauth import OAuth1Service

class ApiClient:
    __attrs__ = ['consumer_key', 'consumer_secret']

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.service = OAuth1Service(name='bricklink',
                                     consumer_key=consumer_key,
                                     consumer_secret=consumer_secret,
                                     base_url='https://api.bricklink.com/api/store/v1/')

        self.session = self.service.get_session((access_token, access_token_secret))

    def processResponse(self, response):
        if not 'meta' in response:
            raise BricklinkInvalidResponseException('No meta and/or data key in response')

        meta = response['meta']
        if meta['code'] not in (200, 201, 204):
            if meta['message'] == 'INVALID_URI': raise BricklinkInvalidURIException(meta['description'])
            elif meta['message'] == 'INVALID_REQUEST_BODY': raise BricklinkInvalidRequestBodyException(meta['description'])
            elif meta['message'] == 'PARAMETER_MISSING_OR_INVALID': raise BricklinkParameterMissingOrInvalidException(meta['description'])
            elif meta['message'] == 'BAD_OAUTH_REQUEST': raise BricklinkBadOauthRequestException(meta['description'])
            elif meta['message'] == 'PERMISSION_DENIED': raise BricklinkPermissionDeniedException(meta['description'])
            elif meta['message'] == 'RESOURCE_NOT_FOUND': raise BricklinkResourceNotFoundException(meta['description'])
            elif meta['message'] == 'METHOD_NOT_ALLOWED': raise BricklinkMethodNotAllowedException(meta['description'])
            elif meta['message'] == 'UNSUPPORTED_MEDIA_TYPE': raise BricklinkUnsupportedMediaTypeException(meta['description'])
            elif meta['message'] == 'RESOURCE_UPDATE_NOT_ALLOWED': raise BricklinkResourceUpdateNotAllowedException(meta['description'])
            elif meta['message'] == 'INTERNAL_SERVER_ERROR': raise BricklinkInternalServerErrorException(meta['description'])
            else: raise BricklinkUnspecifiedException(meta['code'], meta['message'], meta['description'])

        data = response['data']
        return data

    def get(self, url, params):
        response = self.session.request('GET', url, True, '', params=params).json()
        return self.processResponse(response)