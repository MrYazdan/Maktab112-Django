import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# logger = logging.getLogger('django.db.backends')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

from book.models import Author, Book, Category, Reader  # noqa:E402

# a1 = Author.objects.get(id=1)
# a1.name = "Aliram"
# a1.save()

# create new data:
# 1)
# Author.objects.create(name="Soltan")
#
# 2)
# a1 = Author(name="Amir Ali")
# a1.save()

# get
# print(Author.objects.get(id=4))

# filter
# print(Author.objects.filter(id__in=[1, 2, 3]))
# qs = Author.objects.filter(id__in=[1, 2, 3])
# print(qs.query)

# all
# qs = Author.objects.all()
# print(qs.query)

# exclude
# qs = Author.objects.exclude(id__in=[1, 2, 3, 4])
# print(qs)
# print(qs.query)

# order_by
# qs = Author.objects.order_by('-name')
# print(qs)
# print(qs.query)

# update
# qs = Author.objects.all().filter(id__gte=10).exclude(name__startswith="M")
# print(qs)

# from django.db.models import F, Value as V
# from django.db.models.functions import Concat
#
# Author.objects.filter(id__gt=10).update(name=Concat(F("id"), V(" - "), F("name")))
#
# for author in Author.objects.filter(id__gt=6):
#     author.name = f"{author.name} - HACKED"
#     author.save()

# count
# count = Author.objects.all().count()
# print(count)
# print(len(Author.objects.all()))

# exists
# print(Author.objects.get(name__startswith="J"))
# print(Author.objects.filter(name__startswith="J"))
# print(Author.objects.filter(name__startswith="J").exists())

# earliest , latest
# Book.objects.order_by("published_date").first()
# Book.objects.earliest("published_date")
#
# Book.objects.order_by("published_date").last()
# Book.objects.latest("published_date")

# values
# print(Author.objects.values())
# print(Author.objects.values('name'))

# values_list
# print(Author.objects.values_list())
# print(Author.objects.values_list('name'))
# print(Author.objects.values_list('name', flat=True))

# only # TODO : RESEARCH ...
# print(Author.objects.only('name').filter(name__startswith="M"))
# print(Book.objects.only('title').filter(price__gte=10))  # Warn !!!

# defer # TODO : RESEARCH ...
# print(Author.objects.defer('name').filter(name__startswith="M")) # Warn !!!
# print(Author.objects.defer('name').filter(id__gte=10))

# select_related (Join => Foreign key)
# TODO : Example ...


# prefetch_related (Join => M2M)
# TODO : Example ...

# annotate
# from django.db.models import F, Value as V
# from django.db.models.functions import Concat
#
# print(*[r.fullname for r in Reader.objects.all()], sep="\n")
# print(*Reader.objects.values(), sep="\n")
#
# print(*Reader.objects.annotate(fullname=Concat(F("first_name"), V(" "), F("last_name"))).values(), sep="\n")

# distinct
# print(Reader.objects.distinct())

# Create user:
# from django.contrib.auth.models import User

# user = User.objects.create(username="maktab_u1", password="123")  # Warning !!!
# user.set_password("123")
# user.save()

# Best P:
# user = User.objects.create_user("maktab_u2", password="123")