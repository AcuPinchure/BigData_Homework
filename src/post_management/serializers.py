from rest_framework import serializers

from .models import Post, RankItem


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'category', 'main_image', 'publish_date', 'last_modify', 'modify_user', 'intro_title', 'intro_content']

class RankItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankItem
        fields = ['id', 'sort_index', 'title', 'content']