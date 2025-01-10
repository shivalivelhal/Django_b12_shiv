from django.db import models


# Create your models here.
# in flask we enter id and all by own,but in django no need to declare,by default django do that
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email =models.EmailField(unique=True)
    mobile_num = models.IntegerField(unique=True)
    designation = models.CharField(max_length=100)
    salary =models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.salary}"
    
    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "employee"        
                           #appname_class name in small letter eg.app1_employee but we given name so create by this name
                                           
                                           


