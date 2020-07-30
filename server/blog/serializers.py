from rest_framework import serializers
from .models import Blog, comment


class CommentSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer()

    class Meta:
        model = comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content',
                  'image', 'created_at', 'comments']
