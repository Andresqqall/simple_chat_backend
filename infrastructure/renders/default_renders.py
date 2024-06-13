from rest_framework.renderers import JSONRenderer


class DefaultJSONRenderer(JSONRenderer):
    charset = 'utf-8'
