from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffSetPaginations(LimitOffsetPagination):
    default_limit = 5
