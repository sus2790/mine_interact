__all__ = (
    'ChannelNotFound',
    'APIError',
    'APITimeout',
)

class ChannelNotFound(Exception):
    pass
  
class APIError(Exception):
    pass

class APITimeout(Exception):
    pass
