from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Wallet(models.Model):
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	balance=models.IntegerField(default=0)

class Transaction(models.Model):
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	transaction=models.CharField(max_length=50,default="")
	amount=models.IntegerField(default=0)
	trans_date=models.DateTimeField(default=timezone.now)
