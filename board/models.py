from django.db import models
from acc.models import User
# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likey")
    content = models.TextField()
    pubdate = models.DateTimeField()
    likey=models.ManyToManyField(User, blank=True related_name="likey")

    def __str__(self):
        return self.subject