from api import models
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.validators import ValidationError


# a.查看所有学位课并打印学位课名称以及授课老师
# class CourseSerializer(serializers.ModelSerializer):
#     teacher_obj = serializers.SerializerMethodField()
#
#     class Meta:
#         model = models.DegreeCourse
#         fields = ['id', 'name', 'teacher_obj']
#
#     def get_teacher_obj(self, row):
#         teacher = row.teachers.all()
#         return [{'name': item.name} for item in teacher]


# b.查看所有学位课并打印学位课名称以及学位课的奖学金
# class CourseSerializer(serializers.ModelSerializer):
#     degree_course = serializers.CharField(source='degree_course.name')
#     class Meta:
#         model = models.Scholarship
#         fields = ['id', 'name', 'value', 'degree_course']

    # def get_bonus(self, ret):

# c.展示所有的专题课
# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Course
#         fields = "__all__"


 # d. 查看id=1的学位课对应的所有模块名称
# class DegreeCourseSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.DegreeCourse
#         fields = ['id', 'name', '']


# i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
class DegreeCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', '']