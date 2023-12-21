from django.db import models
from django.contrib.auth.models import AbstractUser
import pandas as pd
import joblib,os

class CustomUser(AbstractUser):
    level = models.IntegerField(blank=True,default=0)
    income = models.IntegerField(default=0)
    expense = models.IntegerField(default=0)
    asset = models.IntegerField(default=0)
    loan=models.IntegerField(default=0)
    financial_goal = models.CharField(max_length=50)
    def save(self,*args, **kwargs) -> None:
            # abishai model classify madi level na set madutte
        loaded_model = joblib.load(os.path.join('ML','random_forest_classifier_model.pkl'))
        user_data = pd.DataFrame([[self.asset,self.income, self.loan]], columns=['asset', 'income', 'loan amount'])
        predicted_level = loaded_model.predict(user_data)
        self.level=predicted_level[0]
        return super().save(*args,**kwargs)


class Investment(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    description = models.TextField()
    def save(self,*args,**kwargs):
        # send notifications
        super().save(*args,**kwargs)
    def __str__(self) -> str:
        return self.name


class Insurance(models.Model):
    name= models.CharField(max_length=50)
    Type = models.IntegerField(default=0)
    description=models.TextField()    
    level=models.IntegerField()

    def save(self,*args,**kwargs):
        # send notifications
        super().save(*args,**kwargs)


class Consultancy(models.Model):
    name= models.CharField(max_length=50)
    Type = models.IntegerField(default=0)
    description=models.TextField()    
    level=models.IntegerField()

    def save(self,*args,**kwargs):
        # send notifications
        super().save(*args,**kwargs)


