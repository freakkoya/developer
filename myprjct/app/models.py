from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name 
    
# class Students(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     place = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

        