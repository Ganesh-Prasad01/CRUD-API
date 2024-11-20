from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 100, null = True, blank = True)
    last_name = models.CharField(max_length = 100, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    phone = models.CharField(max_length = 11, null = True, blank = True)
    dob = models.DateField(null = True, blank = True)

    class Meta:
        db_table = "student_info"