from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=30,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    text = models.TextField(null=True)
    def __str__(self):
        return self.title
