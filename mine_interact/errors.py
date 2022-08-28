__all__ = (
    'NotFound',
    'APIError',
    'APITimeout',
)

class NotFound(Exception):
    pass
  
class APIError(Exception):
    pass

class APITimeout(Exception):
    pass
