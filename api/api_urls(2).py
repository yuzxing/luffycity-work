from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.contrib import admin
from api.views import course2

urlpatterns = [
    url(r"^courses/$", course2.CourseView.as_view({'get': 'list', 'post': 'create'})),
    url(r"^courses/(?P<pk>\d+)/$", course2.CourseView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),


]
# router = DefaultRouter()
# router.register(r"course", views.CourseViewSet)
# router.register(r"course_detail", views.CourseDetailViewSet)
# urlpatterns += router.urls
