from .models import Book, Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name",)


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     from uuid import uuid4
    #
    #     return dict(
    #         id=uuid4().hex,
    #         name=data["title"],
    #         price=data['price'],
    #     )




