# skills/admin.py

from django.contrib import admin
from skills.models import Department, Employee, Skill, EmployeeSkill

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(EmployeeSkill)


# Register your models here.
