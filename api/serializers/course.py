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
#     degree_course = serializers.SerializerMethodField()
#     class Meta:
#         model = models.Course
#         fields = ['id', 'name', 'degree_course']
#
#     def get_degree_course(self, ret):
#         course_list = ret.degree_course.all()
#         return [{'name': item.name} for item in course_list]

# i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
# class DegreeCourseSerializer(serializers.ModelSerializer):
#     price_list = serializers.SerializerMethodField()
#     class Meta:
#         model = models.DegreeCourse
#         fields = ['id', 'name', 'price_list']
#
#     def get_price_list(self, ret):
#         price_obj = ret.degreecourse_price_policy.all()
#         return [{'price': item.price} for item in price_obj]


#  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class DegreeCourseSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    degree_course = serializers.SerializerMethodField()
    why_study = serializers.CharField(source='course.why_study')
    what_to_study_brief = serializers.CharField(source='course.what_to_study_brief')
    recommend_courses = serializers.CharField(source='course.recommend_courses')
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'level_name', 'degree_course', 'recommend_courses', 'why_study', 'what_to_study_brief']
