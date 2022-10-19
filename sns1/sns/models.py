from django.db import models
from django.contrib.auth.models import User

# Messageクラス

class Message(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, relatede_name='message_owner')
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

# Create your models here.
