from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from django.contrib import admin
from api.views import course1

urlpatterns = [
    # url(r"^courses/$", course.CourseView.as_view()),
    url(r"^courses/(?P<pk>\d+)/$", course1.CourseView.as_view()),
    url(r"^degree/$", course1.CourseDetailView.as_view())

]
# router = DefaultRouter()
# router.register(r"course", views.CourseViewSet)
# router.register(r"course_detail", views.CourseDetailViewSet)
# urlpatterns += router.urls
