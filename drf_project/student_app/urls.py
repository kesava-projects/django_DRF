from django.urls import path
from .views import student_view, update_student, delete_student, get_student, get_students

urlpatterns = [
    path('operations', student_view),
    path('update/<int:id>', update_student),
    path('delete/<int:id>', delete_student),
    path('view/<int:id>', get_student),
    path('view_all/', get_students)
]
