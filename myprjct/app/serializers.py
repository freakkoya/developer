from rest_framework import serializers
from .models import Course

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# class StudentsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Students
#         fields = '__all__'