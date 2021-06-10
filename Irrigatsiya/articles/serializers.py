from rest_framework import serializers
from .models import Articles
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('name', 'file', 'link','author_id')
    
        def __init__(self):
            model = Articles
            self.instance.author = self.request.user
            fields = ('name', 'file', 'link')
            return super().__init__(**kwargs)

    # current_user = serializers.SerializerMethodField('_user')

    # # Use this method for the custom field
    # def _user(self, obj):
    #     request = self.context.get('request', None)
    #     if request:
    #         return request.user
    def create(self, validated_data):
        # def get_object(self):
        #     author = User.objects.get()
        return Articles.objects.create(**validated_data, author_id=1)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('title', instance.name) 
        instance.file = validated_data.get('file', instance.file)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author',instance.author)
        instance.save()
        return instance

