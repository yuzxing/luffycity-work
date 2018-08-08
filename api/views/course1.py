from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api import models
from api.serializers.course import CourseSerializer, CourseModelSerializer
from api.utils.response import BaseResponse

# api 第一个版本 专题课CBV
class CourseView(APIView):

    def get(self, request, *args, **kwargs):
        # response = {'code': 1000, 'data': None, 'error': None}
        ret = BaseResponse()
        try:
            # 从数据库中取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)

            # 分页之后的结果执行序列化
            ser = CourseSerializer(instance=course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        """增加"""


# 课程详情 CBV
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

    def put(self, request, pk, *args, **kwargs):
        """
        修改
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def delete(self, request, pk, *args, **kwargs):
        """
        删除
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
















