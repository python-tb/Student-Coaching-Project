from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=35)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Teacher(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.first_name + " " + self.last_name



class Course(models.Model):
    course_name = models.CharField(max_length=30)
    fees = models.IntegerField(default=True)
    duration = models.IntegerField(default=True)

    
    def __str__(self):
        return self.course_name