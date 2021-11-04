from django.core.checks.messages import Error
from rest_framework import fields, serializers
from books.models import Author, Book
from django.shortcuts import get_object_or_404


class AuthorSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("custom")
        return super().create(validated_data)

    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "subtitle", "isbn"]

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "author":
                author = Author.objects.get(name=value["name"])
                instance.author = author
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance
