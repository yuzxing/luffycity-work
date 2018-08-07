from django.shortcuts import render
from api import models
from api.utils.response import BaseResponse
from api.serializers.course import DegreeCourseSerializer
from rest_framework.response import Response
from api import serializers as api_serializers
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

# 课程类
# class CourseView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         ret = BaseResponse()
#         try:
#             # 从数据库获取数据
#             queryset = models.Course.objects.all()
#             # 分页
#             page = PageNumberPagination()
#             course_list = page.paginate_queryset(queryset, request, self)
#
#             # 分页之后的结果执行序列化
#             ser = CourseSerializer(instance=course_list, many=True)
#             ret.data = ser.data
#         except Exception as e:
#             ret.code = 500
#             ret.error = '获取数据失败'
#         return Response(ret.dict)

    # def get(self, request, *args, **kwargs):
    #     course_list = models.Course.objects.all()
    #     ret = CourseSerializer(instance=course_list, many=True)
    #     return Response(ret.data)


#  课程详细类
# class CourseDetailView(APIView):
#
#     def get(self, request, pk, *args, **kwargs):
#         response = {'code': 1000, 'data': None, 'error': None}
#         try:
#             course = models.Course.objects.get(id=pk)
#             ser = CourseSerializer(instance=course)
#             response['data'] = ser.data
#         except Exception as e:
#             response['code'] = 500
#             response['error'] = '获取数据失败'
#         return Response(response)
#
#
# # 学位课类
# class DegreeCourseView(APIView):
#     # a.查看所有学位课并打印学位课名称以及授课老师
#     def get(self, request, *args, **kwargs):
#         response = {'code': 1000, 'data': None, 'error': None}
#         try:
#             course = models.DegreeCourse.objects.all()
#             ser = DegreeCourseView(instance=course)
#             response['data'] = ser.data
#         except Exception as e:
#             response['code'] = 500
#             response['error'] = '获取数据失败'
#         return Response(response)

# c.展示所有的专题课
# class DegreeCourseView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         course_list = models.Course.objects.all()
#         ret = CourseSerializer(instance=course_list, many=True)
#         return Response(ret.data)


# d. 查看id=1的学位课对应的所有模块名称
class DegreeCourseView(APIView):

    def get(self, request, *args, **kwargs):
        course_list = models.DegreeCourse.objects.filter(id=1).first()
        ret = DegreeCourseSerializer(instance=course_list)
        return Response(ret.data)



























# 课程详细类
class CourseDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        course = models.Course.objects.get(id=pk)
        res = CourseSerializer(instance=course)
        return Response(res.data)
