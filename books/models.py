from django.db import models

class Komil:
    pass

class Book(models.Model):
    title = models.CharField(max_length=233)
    subtitle = models.CharField(max_length=233)
    author = models.CharField(max_length=233)
    isbn = models.CharField(max_length=233)

    def __str__(self):
        return self.title