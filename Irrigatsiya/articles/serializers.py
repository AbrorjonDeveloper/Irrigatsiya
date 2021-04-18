from rest_framework import serializers
from .models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('name', 'article', 'link',)
    
        def __init__(self):
            model = Articles
            fields = ('name', 'article', 'link',)
            return super().__init__(**kwargs)

    def create(self, validated_data):
        return Articles.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name) 
        instance.article = validated_data.get('article', instance.article)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

