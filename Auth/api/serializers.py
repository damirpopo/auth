from rest_framework import serializers
from .models import Student,Subject,Class

class Studentserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Student
        fields = '__all__'

class Subjectserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Subject
        fields = '__all__'

class Classserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Class
        fields = '__all__'