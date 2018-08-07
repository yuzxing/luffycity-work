from django.contrib import admin
from api import models
# Register your models here.
admin.site.register(models.CourseCategory)  # 课程大类
admin.site.register(models.CourseSubCategory)  # 课程子类
admin.site.register(models.DegreeCourse)  # 学位课程
admin.site.register(models.Teacher)  # 老师表
admin.site.register(models.Scholarship)  # 学位课程奖金表
admin.site.register(models.Course)  # 课程
admin.site.register(models.CourseDetail)  # 课程详情表
admin.site.register(models.OftenAskedQuestion)  # 常见问题表
admin.site.register(models.CourseOutline)  # 课程大纲表
admin.site.register(models.CourseChapter)  # 课程章节表
admin.site.register(models.CourseSection)  # 课程目录表
admin.site.register(models.Homework)  # 作业表
admin.site.register(models.PricePolicy)  # 价格策略表
