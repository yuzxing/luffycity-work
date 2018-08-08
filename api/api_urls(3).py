from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.contrib import admin
from api.views import course3

urlpatterns = [
    url(r"^courses/$", course3.CourseView.as_view({'get': 'list'})),
    url(r"^courses/(?P<pk>\d+)/$", course3.CourseView.as_view({'get': 'retrieve'})),

]
# router = DefaultRouter()
# router.register(r"course", views.CourseViewSet)
# router.register(r"course_detail", views.CourseDetailViewSet)
# urlpatterns += router.urls
