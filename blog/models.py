from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete="CASCADE")
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] # 100글자를 상한선으로 해서 리턴