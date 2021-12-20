from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    question = models.CharField(max_length=200, default="")
    question_description = models.TextField()
    question_answer = models.CharField(max_length=200)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Points(models.Model):
    user = models.ForeignKey(
        User, related_name="points", on_delete=models.CASCADE)
    total_point = models.IntegerField(default=0)


class Answer(models.Model):
    user = models.ForeignKey(
        User, related_name="answer", on_delete=models.CASCADE)

    question = models.ForeignKey(
        "question", related_name="answer", on_delete=models.CASCADE)
