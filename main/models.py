from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    TYPE_CHOICES = (('B', 'Bullet'), ('F', 'Food'), ('T', 'Travel'), ('S', 'Sport'))

    type = models.CharField(choices=TYPE_CHOICES, max_length=1)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
