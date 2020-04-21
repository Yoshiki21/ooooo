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
