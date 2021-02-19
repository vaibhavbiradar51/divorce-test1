from django.db import models

# Create your models here.

class Divorce(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    State_issued_divorce_id = models.CharField(max_length=100, null=True,blank=True)
    Date_of_birth = models.CharField(max_length=100, null=True,blank=True)
    Nationality = models.CharField(max_length=100, null=True,blank=True)
    Maritial_status = models.CharField(max_length=100, null=True,blank=True)
    Highest_education = models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
    	return 'Record - '+str(self.sno)
