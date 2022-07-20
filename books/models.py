from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    featured = models.BooleanField(default=False)

class TrackedBook(BaseModel):
    # Status Choices
    WANT_TO_READ = 'WTR'
    READING = 'R'
    READ = 'RD'
    STATUS_CHOICES = [
        (WANT_TO_READ, 'Want to Read'),
        (READING, 'Reading'),
        (READ, 'Read'),
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=WANT_TO_READ,
    )

class Note(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    note = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=False)
