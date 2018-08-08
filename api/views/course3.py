from rest_framework.response import Response
from api import models
from api.serializers.course import CourseSerializer, CourseModelSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin


# 第三个版本
class CourseView(ListModelMixin, GenericViewSet):
    queryset = models.Course.objects.all()

    def list(self, request, *args, **kwargs):
        course_list = models.Course.objects.all()
        ser = CourseModelSerializer(instance=course_list, many=True)
        return Response(ser.data)
