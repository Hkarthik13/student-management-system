from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
