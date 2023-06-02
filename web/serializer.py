from rest_framework import serializers

from web.models import user, academy, teacher, course, course_resource, keyword, forum, comment, sensitive_word
from web.models.courseclick import CourseClick
from web.models.forum_click import ForumClick


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user.User
        exclude = ['password']

    def to_representation(self, value):
        data = super().to_representation(value)
        return data


class AcademySerializer(serializers.ModelSerializer):
    class Meta:
        model = academy.Academy
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course.Course
        fields = "__all__"

    def to_representation(self, value):
        data = super().to_representation(value)
        data['keyword'] = [item.keyword for item in value.keyword.all()]
        data['teacher'] = value.teacher.name
        data['clicks'] = CourseClick.objects.filter(course=value).count()
        return data


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = teacher.Teacher
        exclude = ['password']


class CourseResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_resource.CourseResource
        fields = "__all__"


class KeywordSerializer(serializers.ModelSerializer):
    clicks = serializers.IntegerField()

    class Meta:
        model = keyword.Keyword
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment.Comment
        fields = "__all__"

    def to_representation(self, value):
        data = super().to_representation(value)
        data['user'] = UserSerializer(value.user).data
        return data


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = forum.Forum
        fields = "__all__"

    def to_representation(self, value):
        data = super().to_representation(value)
        data['user'] = {'id': value.user.id, 'nickname': value.user.nickname, "head": '/media/' + value.user.head.name}
        data['keyword'] = [item.keyword for item in value.keyword.all()]
        data['clicks'] = ForumClick.objects.filter(forum=value).count()
        return data


class ForumImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = forum.ForumImg
        fields = "__all__"


class SensitiveWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensitive_word.SensitiveWord
        fields = "__all__"
