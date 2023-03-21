from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('class/', ClassList.as_view()),
    path('class/<int:pk>/', ClassUpdate.as_view()),
    path('classdel/<int:pk>/', ClassDestroy.as_view()),
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentUpdate.as_view()),
    path('studentdel/<int:pk>/', StudentDestroy.as_view()),
    path('subject/', SubjectList.as_view()),
    path('subject/<int:pk>/', SubjectUpdate.as_view()),
    path('subjectdel/<int:pk>/', SubjectDestroy.as_view()),
    path('auth/', include('rest_framework.urls')),
    path('auth2/',include('djoser.urls')),
    re_path(r'^auth2',include('djoser.urls.authtoken'))
]