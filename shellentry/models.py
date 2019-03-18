from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 30)
	college = models.CharField(max_length = 50)
	age = models.IntegerField()
	phone_no = models.CharField(max_length =25)

class Book(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    author = models.CharField(max_length = 30)
    price = models.IntegerField()
    publisher = models.CharField(max_length =25)
	
	


