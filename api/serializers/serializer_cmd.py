from rest_framework import serializers
from api import models


class CourseSerializers(serializers.Serializer):  # API接口的序列化
    id = serializers.IntegerField()
    name = serializers.CharField()


class CourseModelSerializers(serializers.ModelSerializer):

    # c.展示所有的专题课
    course_list = serializers.CharField(source='get_course_type_display')

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    level = serializers.CharField(source="get_level_display")
    why_study = serializers.CharField(source="coursedetail.why_study")
    what_to_study_brief = serializers.CharField(source="coursedetail.what_to_study_brief")
    recommend_courses = serializers.SerializerMethodField()

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    querist = serializers.SerializerMethodField()

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    CourseOutline = serializers.SerializerMethodField()

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    CourseChapter = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'level', 'teacher_name', 'course_list', 'why_study', 'recommend_courses',
                  'what_to_study_brief',
                  'querist',
                  'CourseOutline',
                  'CourseChapter',
                  ]

    def get_recommend_courses(self, res):
        res_list = res.coursedetail.recommend_courses.all()
        set = [{'id': item.id, "name": item.name} for item in res_list]
        return set

    def get_querist(self, res):
        res_list = res.asked_question.all()
        set = [{'id': item.id, 'question': item.question, "answer": item.answer} for item in res_list]
        return set

    def get_CourseOutline(self, ret):
        ret_list = ret.coursedetail.courseoutline_set.all()
        set = [{'id': item.id, 'title': item.title, "content": item.content} for item in ret_list]
        return set

    def get_CourseChapter(self, res):
        res_list = res.coursechapters.all()
        set = [{'id': item.id, 'name': item.name, "chapter": item.chapter, "summary": item.summary} for item in
               res_list]
        return set


class DegreeCourseModelSerializersPrice(serializers.ModelSerializer):
    # a.查看所有学位课并打印学位课名称以及授课老师
    teacher_name = serializers.SerializerMethodField()

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    value_dree = serializers.SerializerMethodField()

    # d. 查看id=1的学位课对应的所有模块名称
    degree_model_name = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse
        fields = ['id', 'name', 'value_dree', 'degree_model_name', 'teacher_name']

    def get_degree_model_name(self, res):
        res_list = res.course_set.all()
        set = [{'id': item.id, 'name': item.name} for item in res_list]
        return set

    def get_value_dree(self, res):
        res_list = res.scholarship_set.all()
        set = [{'id': item.id, 'value': item.value} for item in res_list]
        return set

    def get_teacher_name(self, res):
        res_list = res.teachers.all()
        set = [{'id': item.id, "name": item.name} for item in res_list]
        return set