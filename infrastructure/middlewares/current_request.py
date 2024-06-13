""" Middleware to provide current request user """
from threading import current_thread

from django.utils.deprecation import MiddlewareMixin

_requests = {}


def current_request():
    return _requests.get(current_thread().ident, None)


class RequestMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        _requests[current_thread().ident] = request

    @staticmethod
    def process_response(request, response):
        _requests.pop(current_thread().ident, None)
        return response

    @staticmethod
    def process_exception(request, exception):
        _requests.pop(current_thread().ident, None)
        raise exception
