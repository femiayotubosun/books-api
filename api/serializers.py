from rest_framework import serializers
from books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "subtitle", "isbn"]

    def create(self, validated_data):
        try:
            author = Author.objects.get(name=validated_data["author"]["name"])
        except Author.DoesNotExist:
            raise serializers.ValidationError({"author": "This author does not exist."})
        del validated_data["author"]
        book = Book.objects.create(**validated_data, author=author)
        return book

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "author":
                try:
                    author = Author.objects.get(name=value["name"])
                except Author.DoesNotExist:
                    raise serializers.ValidationError(
                        {"author": "This author does not exist"}
                    )

                instance.author = author
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance
