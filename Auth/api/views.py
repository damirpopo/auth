from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from .models import Student,Subject,Class
from rest_framework.authentication import TokenAuthentication
from .serializers import Studentserializer,Classserializer,Subjectserializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class StudentUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Studentserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class StudentDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Studentserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ClassList(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = Classserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ClassUpdate(RetrieveUpdateAPIView):
    queryset = Class.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Classserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ClassDestroy(RetrieveDestroyAPIView):
    queryset = Class.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Classserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubjectList(ListCreateAPIView):
    queryset = Subject.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Subjectserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubjectUpdate(RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Subjectserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SubjectDestroy(RetrieveDestroyAPIView):
    queryset = Subject.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Subjectserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
