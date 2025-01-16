from django.shortcuts import render
from skills.models import Employee, Skill, EmployeeSkill

def employee_list(request):
    # Fetch all employees
    employees = Employee.objects.all()
    
    # You can remove this if not using skills directly in the template
    # skills = Skill.objects.all()
    
    # Render the template with employees data
    return render(request, 'employee_list.html', {'employees': employees})
