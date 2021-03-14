from django.db import models

class employees(models.Model):
    f_name = models.CharField(max_length=10)
    l_name =models.CharField(max_length=10)
    emp_id = models.IntegerField()
    
    def __str__ (self):
        return self.fname
         