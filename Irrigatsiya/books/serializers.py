from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'file', 'link')
        
    def create(self, validated_data):
        return Book.objects.create(**validated_data, author_id=1)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.link = validated_data.get('link', instance.link)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
    


        
