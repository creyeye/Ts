from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=100)


class Category(models.Model):
    category = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
