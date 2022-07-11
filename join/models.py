from datetime import datetime

from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    userid=models.CharField(max_length=18, unique=True)
    passwd=models.CharField(max_length=18)
    name=models.CharField(max_length=18)
    nickname=models.CharField(max_length=18)
    phone=models.CharField(max_length=15)
    email=models.TextField()
    mailing=models.BooleanField(default=False)
    zipcode=models.IntegerField()
    addr = models.TextField()
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table='member'