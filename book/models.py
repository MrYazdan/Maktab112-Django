from django.db import models
from django.core.validators import MinValueValidator

from core.models import Image, BaseImage, TimeStampMixin


class Profile(TimeStampMixin):
    bio = models.TextField()
    author = models.OneToOneField("Author", on_delete=models.CASCADE)


class Author(TimeStampMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.id} - {self.name}>"


class Book(TimeStampMixin):
    title = models.CharField(max_length=180, blank=False)
    published_date = models.DateField(null=True)
    price = models.FloatField(validators=[
        MinValueValidator(0)
    ])
    authors = models.ManyToManyField(Author, blank=True)
    is_available = models.BooleanField(default=True)
    categories = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return self.title


# class BookCover(Image):
#     book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="images")

class BookCover(BaseImage):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="images")


class NewestBook(Book):
    class Meta:
        proxy = True
        ordering = ["-created_at"]


class Category(TimeStampMixin):
    name = models.CharField(max_length=200, blank=False)
    parent = models.ForeignKey("self", related_name="children", on_delete=models.SET_NULL, default=None, null=True,
                               blank=True)

    # tree relation - self relation - recursive relation

    def __str__(self):
        return f"{self.name}"


class Reader(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
