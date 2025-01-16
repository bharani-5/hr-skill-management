# skills/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')])

    def __str__(self):
        return f"{self.employee} - {self.skill}"



# Create your models here.
