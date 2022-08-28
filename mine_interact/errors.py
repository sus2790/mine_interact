__all__ = (
    'ChannelNotFound',
    'UserNotFound',
    'APIError',
    'APITimeout',
)

class ChannelNotFound(Exception):
    pass

class UserNotFound(Exception):
    pass
  
class APIError(Exception):
    pass

class APITimeout(Exception):
    pass
