from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  Question(models.Model):
    text = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
    
class QuizAttempt(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now_add=True)