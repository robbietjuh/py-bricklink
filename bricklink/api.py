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
        if not ('code', 'message', 'description', 'data') in response:
            raise BricklinkInvalidResponseException('No status code in response')

        if response['code'] not in (200, 201, 204):
            if response['message'] == 'INVALID_URI': raise BricklinkInvalidURIException(response['description'])
            elif response['message'] == 'INVALID_REQUEST_BODY': raise BricklinkInvalidRequestBodyException(response['description'])
            elif response['message'] == 'PARAMETER_MISSING_OR_INVALID': raise BricklinkParameterMissingOrInvalidException(response['description'])
            elif response['message'] == 'BAD_OAUTH_REQUEST': raise BricklinkBadOauthRequestException(response['description'])
            elif response['message'] == 'PERMISSION_DENIED': raise BricklinkPermissionDeniedException(response['description'])
            elif response['message'] == 'RESOURCE_NOT_FOUND': raise BricklinkResourceNotFoundException(response['description'])
            elif response['message'] == 'METHOD_NOT_ALLOWED': raise BricklinkMethodNotAllowedException(response['description'])
            elif response['message'] == 'UNSUPPORTED_MEDIA_TYPE': raise BricklinkUnsupportedMediaTypeException(response['description'])
            elif response['message'] == 'RESOURCE_UPDATE_NOT_ALLOWED': raise BricklinkResourceUpdateNotAllowedException(response['description'])
            elif response['message'] == 'INTERNAL_SERVER_ERROR': raise BricklinkInternalServerErrorException(response['description'])
            else: raise BricklinkUnspecifiedException(response['code'], response['message'], response['description'])

        return response['data']

    def get(self, url, params):
        response = self.session.request('GET', url, True, '', params=params).json()
        return self.processResponse(response)