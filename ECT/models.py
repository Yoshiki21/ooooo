from django.db import models

# Create your models here.

class Meeting(models.Model):
    date = models.DateTimeField()
    def __str__(self):
        return str(self.date.date())

class Topic(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    topic_text = models.CharField(max_length=200)
    def __str__(self):
        return self.topic_text

class Expression(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    expression_text = models.CharField(max_length=200)
    def __str__(self):
        return self.expression_text

class Member(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name