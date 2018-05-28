"""
Exceptions
"""


class BaseException(Exception):
    message = "An unknown exception occurred."

    def __init__(self, **kwargs):
        try:
            super(BaseException, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            if not self.is_fatal_exception():
                super(BaseException, self).__init__(self.message)

    def __str__(self):
        return self.msg


class ResourceNotFound(BaseException):
    message = "Could not find %(resource_type)s: %(unique_key)s"

    def __init__(self, model, unique_key):
        resource_type = model.__name__.lower()
        super(ResourceNotFound, self).__init__(resource_type=resource_type,
                                               unique_key=unique_key)


class MissParam(BaseException):
    message = "Missing %(param_type)s"

    def __init__(self, param_name):
        super(ResourceNotFound, self).__init__(param_type=param_name)

