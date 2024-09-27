from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # This will list employees
    path('create/', views.create_employee, name='create_employee'),  # This will create a new employee
    path('update/<int:pk>/', views.update_employee, name='update_employee'),  # This will update an employee by id (primary key)
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),  # This will delete an employee by id
]
