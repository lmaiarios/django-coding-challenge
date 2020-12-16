from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    publish_date = models.DateField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)