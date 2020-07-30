from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import BlogSerializer, CommentSerializer

from .pagination import MyLimitOffSetPaginations
from .models import Blog, comment


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = MyLimitOffSetPaginations
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']