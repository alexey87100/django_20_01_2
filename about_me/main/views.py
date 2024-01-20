from django.shortcuts import render
from django.http import Http404

from .data import EMPLOYEES, SKILLS


def index(request):
    """Главная страница."""
    context = {
        'employees': EMPLOYEES
    }
    return render(request, 'index.html', context)


EMPLOYEES_ID = {employee['id']: employee for employee in EMPLOYEES}


def employee(request, employee_id):
    """Страница сотрудника."""
    if employee_id not in EMPLOYEES_ID.keys():
        raise Http404("Нет такого сотрудника")
    employee = EMPLOYEES_ID[employee_id].copy()
    list_skills = []
    for skill_id in employee['skills']:
        for elem in SKILLS:
            if skill_id == elem['id']:
                list_skills.append(elem['name'])
                break
    employee['skills'] = list_skills
    context = {
        'employee': employee
    }
    return render(request, 'employee.html', context)