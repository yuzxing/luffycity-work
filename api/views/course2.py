from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api import models
from api.serializers.course import CourseModelSerializer, CourseSerializer
from api.utils.response import BaseResponse


# api的 第二个版本
class CourseView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.Course.objects.all()
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)
            ser = CourseModelSerializer(instance=course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)

    def create(self, request, *args, **kwargs):
        """增加"""

    def retrieve(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseModelSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

    def update(self, request, pk, *args, **kwargs):
        """修改数据"""
        pass

    def destroy(self, request, *args, **kwargs):
        """删除"""
        pass
