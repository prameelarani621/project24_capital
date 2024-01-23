from django.db import models

# Create your models here.
class Country(models.Model):
    Cid=models.IntegerField(primary_key=True)
    C_Name=models.CharField(max_length=100)
              
                  
class Capital(models.Model):
    Cid=models.IntegerField(primary_key=True)
    C_Name=models.OneToOneField(Country,on_delete=models.CASCADE)
    Capital_Name=models.CharField(max_length=100)


#class Country(models.Model):
 #   cname=models.CharField(max_length=100)
  #  cid=models.ForeignKey(Capital,on_delete=models.CASCADE)



