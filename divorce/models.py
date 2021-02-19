from django.db import models

# Create your models here.

class Divorce(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    State_issued_divorce_id = models.CharField(max_length=100, null=True)
    Date_of_birth = models.CharField(max_length=100, null=True)
    Nationality = models.CharField(max_length=100, null=True)
    Maritial_status = models.CharField(max_length=100, null=True)
    Highest_education = models.CharField(max_length=100, null=True)

    def __str__(self):
    	return self.sno
