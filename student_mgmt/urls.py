from django.urls import path,include # type: ignore
from .views import *

urlpatterns = [
    
    path("", show_panel),
    path('api/get-students-data',StudentData.as_view()),
    path('api/create-student',CreateStudentRecord.as_view()),
    path('api/update-student/<int:id>',UpdateStudentRecord.as_view()),
    path('api/delete-student/<int:id>',RemoveStudentRecord.as_view()),
    
]
