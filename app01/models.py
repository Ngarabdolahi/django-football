from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table="majors"
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    majore = models.ForeignKey(Major,on_delete=models.DO_NOTHING)
    class Meta:
        db_table="teachers"