from django.db import models

# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        abstract = True
        
class Teacher(Common):
    Qualification= models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    
    
class Student(Common):
    Class  = models.IntegerField()
    Total_marks = models.IntegerField()
    Obtain_marks = models.IntegerField()
    Board = models.CharField(max_length=20)
    
# class Courses(models.Model):
#     course_code = models.IntegerField()
#     email = None
#     password = None