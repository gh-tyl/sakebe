from django.db import models
from django.db.models.fields import DateTimeField

class Scream(models.Model):
    content = models.TextField(null=True)
    color = models.IntegerField(null=True)
    expression_points = models.FloatField(null=True)
    decibel = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'scream'

class Comment(models.Model):
    comment_id = models.ForeignKey('Scream', to_field='id', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    class Meta:
        db_table = 'comment'