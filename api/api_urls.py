from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.contrib import admin
from api.views import course

urlpatterns = [
    # url(r"^courses/$", course.CourseView.as_view()),
    url(r"^courses/(?P<pk>\d+)/$", course.CourseDetailView.as_view()),
    url(r"^degree/$", course.DegreeCourseView.as_view())

]
# router = DefaultRouter()
# router.register(r"course", views.CourseViewSet)
# router.register(r"course_detail", views.CourseDetailViewSet)
# urlpatterns += router.urls
