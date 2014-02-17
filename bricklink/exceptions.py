'''
    bricklink.exceptions
    --------------------

    A module providing Bricklink exceptions
'''

class BricklinkInvalidResponseException(Exception): pass


class BricklinkInvalidURIException(Exception): pass


class BricklinkInvalidRequestBodyException(Exception): pass


class BricklinkParameterMissingOrInvalidException(Exception): pass


class BricklinkBadOauthRequestException(Exception): pass


class BricklinkPermissionDeniedException(Exception): pass


class BricklinkResourceNotFoundException(Exception): pass


class BricklinkMethodNotAllowedException(Exception): pass


class BricklinkUnsupportedMediaTypeException(Exception): pass


class BricklinkResourceUpdateNotAllowedException(Exception): pass


class BricklinkInternalServerErrorException(Exception): pass


class BricklinkUnspecifiedException(Exception): pass


class BricklinkInvalidParameterException(Exception): pass