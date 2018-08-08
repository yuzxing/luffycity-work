from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import serializer_cmd
from api.utils.response import BaseResponse
from api import models


class CourseView(APIView):  # API接口的练习 CBV
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            quest = models.Course.objects.all()
            set_res = serializer_cmd.CourseModelSerializers(instance=quest, many=True)
            ret.data = set_res.data
        except Exception as e:
            ret.code = 500
            ret.error = '传输错误'
        return Response(ret.dict)


class CourseModelView(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.Course.objects.get(id=pk)
            ser_quer = serializer_cmd.CourseModelSerializers(instance=queryset)
            ret.data = ser_quer.data
        except Exception as e:
            ret.code = 500
            ret.error = '传输错误'
        return Response(ret.dict)


class DegreeCourseView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            res = models.DegreeCourse.objects.all()
            set_res = serializer_cmd.DegreeCourseModelSerializersPrice(instance=res, many=True)
            ret.data = set_res.data
        except Exception as e:
            ret.code = 500
            ret.error = '传输错误'
        return Response(ret.dict)

class DegreeCourseMoldeView(APIView):

    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.get(id=pk)
            ser_quer = serializer_cmd.DegreeCourseModelSerializersPrice(instance=queryset)
            ret.data = ser_quer.data
        except Exception as e:
            ret.code = 500
            ret.error = '传输错误'

        return Response(ret.dict)