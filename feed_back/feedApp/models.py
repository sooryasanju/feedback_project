from django.db import models
from django.http import HttpResponse


# Create your models here.
class Course(models.Model):
    course = models.CharField(max_length=150)

    def __str__(self):
        return self.course


class Batch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.CharField(max_length=150)

    def __str__(self):
        return self.batch


class Registration(models.Model):
    uname = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    pwd = models.CharField(max_length=150)
    cpwd = models.CharField(max_length=150)

    def __str__(self):
        return self.uname
        # return '{}{}'.format(self.uname,self.pwd)


# class Feedback(models.Model):
#     uname=models.ForeignKey(Registration,on_delete=models.CASCADE)
#     course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
#     topic=models.CharField(max_length=150)
#     feedback=models.CharField(max_length=500)
#     def __str__(self):
#         return self.feedback
# def __str__(self):
#     return '{}{}'.format(self.topic,self.feedback)
class Feedback(models.Model):
    uname = models.ForeignKey(Registration, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    topic = models.CharField(max_length=150)
    feedback = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.feedback
